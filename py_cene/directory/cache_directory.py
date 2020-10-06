from py_cene.analyser import format_text
from py_cene.directory import Directory
from py_cene.index import Index


class CacheDirectory(Directory):
    def __init__(self):
        super().__init__()
        self.indexes = set()
    
    def get_index_names(self):
        return {
            index.get_name()
            for index in self.indexes
        }

    def create_new_index(self, name):
        self.indexes.add(Index(name))

    def write_to_index(self, index_name, documents):
        index = self._get_index(index_name)
        # TODO - implement a writer
        with index as open_index:
            for document_id, document in documents:
                text = format_text(document)
                open_index.write(document_id, text)
        
    def commit_index(self, index_name):
        index = self._get_index(index_name)
        index.commit()

    def search(self, term):
        results = []
        for index in self.indexes:
            with index as open_index:
                results.append(open_index.search(term))
        return results
    
    def _get_index(self, index_name):
        for index in self.indexes:
            if index.get_name() == index_name:
                return index
        raise ValueError(f"Unable to find index with name: {index_name}")