from py_cene.index.segment import Segment


class Index:
    # TODO
    # [x] When commit happens, close segment
    # [x] Fix commit logic
    # [ ] Implement names
    # [x] Support search
    # [x] add isopen support to writing and reading
    def __init__(self, name):
        self.name = name
        
        self.is_open = False
        self.current_segment = None
        self.segments = set()
        self.documents = dict()

    def __enter__(self):
        if self.is_open:
            raise ValueError("Index is already open")
        self.is_open = True
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.is_open = False

    def write(self, document_id, text):
        if not self.is_open:
            raise ValueError("Index must be open to write")
        if not self.current_segment:
            self._generate_new_segment()
        self.current_segment.write(document_id, text)
        self.documents[document_id] = text

    def commit(self):
        self.current_segment.commit()
        self.segments.add(self.current_segment)
        self._generate_new_segment()
    
    def get_segments(self):
        return self.segments

    def get_name(self):
        return self.name

    def search(self, term):
        # TODO - Implement returning the documents affected
        if not self.is_open:
            raise ValueError("Index must be open to search")
        results = dict()
        for segment in self.segments:
            segment_results = segment.search(term)
            _merge_results(segment_results, results)

        return _sort_results(results)

    def _generate_new_segment(self):
        self.current_segment = Segment()


def _merge_results(segment_results, results):
    for term, details in segment_results.items():
        if term not in results:
            results[term] = {}
        for document_id, frequency in details.items():
            if document_id in results[term]:
                results[term][document_id] += frequency
            else:
                results[term][document_id] = 1


def _sort_results(results):
    return {
        term: {
            document_id: frequency
            for document_id, frequency in sorted(
                data.items(),
                key=lambda item: item[1],
                reverse=True)
        }
        for term, data in results.items()
        for document_id, frequency in data.items()
    }