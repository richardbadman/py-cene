from abc import ABC, abstractmethod


class Field(ABC):
    def __init__(self, name, value, store=False, index=True):
        self.name = name
        self.value = value
        self.store = store
        self.index = index
        self._process()

    def set_stored(self, boolean):
        self.store = boolean
        
    def set_indexed(self, boolean):
        self.index = boolean

    @abstractmethod
    def _process(self):
        pass