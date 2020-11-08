from abc import ABC, abstractmethod


class Segment(ABC):
    def __init__(self):
        self.dictionary = dict()
    
    @abstractmethod
    def write(self, document_id, **kwargs):
        pass

    @abstractmethod
    def merge(self, other):
        if isinstance(other, Segment):
            pass
        raise ValueError(f"Expected other Segment type, got {type(other)}")