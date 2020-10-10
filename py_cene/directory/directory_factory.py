from py_cene.directory.cache_directory import CacheDirectory
from py_cene.directory.persistant_directory import PersistantDirectory


class DirectoryFactory:
    def create(self, type):
        if type == "CACHE":
            return self._create_cache_directory()
        elif type == "PERSISTANT":
            return self._create_persistant_directory()
        else:
            raise ValueError("Invalid Directory Type")
    
    def _create_cache_directory(self):
        return CacheDirectory()
    
    def _create_persistant_directory(self):
        return PersistantDirectory()