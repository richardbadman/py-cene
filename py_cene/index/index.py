from py_cene.index.segment import Segment


class Index:
    # TODO
    # [x] When commit happens, close segment
    # [x] Fix commit logic
    # [x] Support search
    # [x] add isopen support to writing and reading
    def __init__(self):
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
        if not self.current_segment:
            raise ValueError("No segment to commit")
        self.current_segment.commit()
        self.segments.add(self.current_segment)
        self._generate_new_segment()
    
    def get_segments(self):
        return self.segments

    def search(self, term):
        if not self.is_open:
            raise ValueError("Index must be open to search")

        return {
            document_id: frequency
            for segment in self.segments
            for document_id, frequency in segment.search(term).items()
        }

    def _generate_new_segment(self):
        self.current_segment = Segment()