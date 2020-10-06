from py_cene.directory import (
    CacheDirectory,
    PersistantDirectory
)


class DirectoryFactory:
    def __init__(self):
        self.directory = None
    
    def create(self, type):
        if type == "CACHE":
            return self._create_cache_directory()
        elif type == "PERSISTANT":
            pass
        else:
            raise ValueError("Invalid Directory Type")
    
    def _create_cache_directory(self):
        return CacheDirectory()
    
    def _create_persistant_directory(self):
        pass