from abc import ABC, abstractmethod


class Directory(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create(self):
        pass