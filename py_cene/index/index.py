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

    def commit(self):
        self.current_segment.commit()
        self.segments.add(self.current_segment)
        self._generate_new_segment()
    
    def get_segments(self):
        return self.segments

    def search(self, term):
        if not self.is_open:
            raise ValueError("Index must be open to search")
        results = dict()
        for segment in self.segments:
            current_results = segment.search(term)
            _merge_results(current_results, results)
        return results

    def _generate_new_segment(self):
        self.current_segment = Segment()


def _merge_results(new_results, results):
    for term, data in new_results.items():
        if term in results:
            results[term]["frequency"] += data["frequency"]
            results[term]["documents"] = list(
                set(results[term]["documents"]).union(set(data["documents"]))
            )
        else:
            results[term] = data