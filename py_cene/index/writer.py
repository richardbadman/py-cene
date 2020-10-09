import uuid

from py_cene.analyser import format_text


class IndexWriter:
    # TODO
    # [ ] - write locks?
    # [ ] - give logic to directory to make it bound to this class
    def __init__(self, directory):
        self.directory = directory
        
    def add_document(self, document):
        # TODO - Make it so only this method can write
        # TODO - append document to directory upon successful indexing
        text = format_text(document)
        document_id = uuid.uuid4().hex
        self.directory.write_to_index(document_id, text, document)

    def commit(self):
        self.directory.commit()