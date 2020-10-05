from py_cene.index.segment import Segment


class Index:
    # TODO
    # [x] When commit happens, close segment
    # [x] Fix commit logic
    # [ ] Implement names
    # [ ] Support search
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
        if not self.current_segment:
            self._generate_new_segment()
        self.current_segment.write(document_id, text)

    def commit(self):
        self.current_segment.commit()
        self.segments.add(self.current_segment)
        self._generate_new_segment()
    
    def get_segments(self):
        return self.segments

    def _generate_new_segment(self):
        self.current_segment = Segment()
