from py_cene.index.segment import Segment


PREFIXES = {
    "one",
    "two",
    "three",
    "four"
}

class Index:
    # TODO
    # [ ] Figure out segment prefixes
    # [ ] When commit happens, close segment
    def __init__(self, name, prefixes_iter=None):
        self.name = name
        if not prefixes_iter:
            self.prefixes_iter = iter(PREFIXES)
        else:
            self.prefixes_iter = prefixes_iter
        
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

    def _generate_new_segment(self):
        try:
            prefix = next(self.prefixes_iter)
            self.current_segment = Segment(prefix)
        except StopIteration:
            raise ValueError("Segment limit reached for this index, unable to create new segment")