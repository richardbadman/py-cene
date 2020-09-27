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
        self.prefix = None
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
        self.current_segment.commit()
        self.segments.add(self.current_segment)
        self._generate_new_segment()
    
    def soft_commit(self):
        self.commit()
        
    def hard_commit(self):
        self._generate_new_prefix()
        self.commit()
    
    def get_segments(self):
        return self.segments

    def _generate_new_prefix(self):
        try:
            self.prefix = next(self.prefixes_iter)
        except StopIteration:
            raise ValueError("Segment limit reached for this index, unable to create new segment")
    
    def _generate_new_segment(self):
        if not self.prefix:
            self._generate_new_prefix()
        self.current_segment = Segment(self.prefix)
