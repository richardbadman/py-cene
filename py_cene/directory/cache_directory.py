from py_cene.directory import Directory
from py_cene.index import Index


class CacheDirectory(Directory):
    def __init__(self):
        super().__init__()
        self.indexes = set()
    
    def get_indexes(self):
        return self.indexes

    def create_new_index(self, name):
        self.indexes.add(Index(name))