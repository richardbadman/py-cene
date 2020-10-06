from abc import ABC, abstractmethod


# pylint: disable=no-member
class Directory(ABC):
    def __init__(self):
        self.__name__ == self.__class__.__name__

    def __repr__(self):
        return self.__name__