import uuid
import zlib

from py_cene.analyser import format_text


class IndexWriter:
    # TODO
    # [ ] - write locks?
    # [ ] - give logic to directory to make it bound to this class
    def __init__(self, directory):
        self.directory = directory
        
    def add_document(self, document):
        # TODO - Make it so only this method can write
        text = format_text(document)
        document_id = uuid.uuid4().hex
        try:
            self.directory.write_to_index(document_id, text)
        except Exception:
            # TODO
            pass
        finally:
            compressed_document = zlib.compress(str.encode(document))
            self.directory.append_document(document_id, compressed_document)

    def commit(self):
        self.directory.commit()