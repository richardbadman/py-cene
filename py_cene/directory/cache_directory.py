from py_cene.analyser import format_text
from py_cene.directory.directory import Directory
from py_cene.index import Index


class CacheDirectory(Directory):
    # TODO
    # [ ] - Imeplement naming
    def __init__(self):
        super().__init__()
        self.index = Index()
        self.documents = dict()
    
    def write_to_index(self, document_id, text, document):
        # TODO - make it so this only works if called by the index_writer
        with self.index as open_index:
            open_index.write(document_id, text)
        self.documents[document_id] = document
            
    def commit(self):
        # TODO - make it so this only works if called by the index_writer
        self.index.commit()

    def search_index(self, term):
        # TODO - make it so this only works if called by the index_writer
        with self.index as open_index:
            return open_index.search(term)

    def get_documents(self, document_ids):
        return [
            document
            for document_id, document in self.documents.items()
            if document_id in document_ids
        ]