import io
import pickle
import uuid
import zlib

from os import listdir, linesep, path

from py_cene.directory.directory import Directory
from py_cene.index import Index


OPEN_DOCUMENT_EXTENSION = ".fdt"
CLOSED_DOCUMENT_EXTENSION = ".fdx"
OPEN_INDEX_EXTENSION = ".tim"
CLOSED_INDEX_EXTENSION = ".tip"

class PersistantDirectory(Directory):
    def __init__(self):
        # TODO - Implement size capping
        super().__init__()
        self.directory_path = None
        self.open_index = None

        self.open_document_file = None
        self.open_index_file = None

        self.closed_document_files = []
        self.closed_index_files = []
    
    def get_directory(self, directory_path):
        # TODO - Need to figure out how to call this better on object creation
        if path.exists(directory_path) and path.isdir(directory_path):
            self.directory_path = directory_path

            all_files = _get_files_in_path(directory_path)
            self.open_document_file = _get_open_file(
                _get_by_extension(all_files, OPEN_DOCUMENT_EXTENSION)
            )
            self.open_index_file = _get_open_file(
                _get_by_extension(all_files, OPEN_INDEX_EXTENSION)
            )

            self.closed_document_files = _get_by_extension(all_files, CLOSED_DOCUMENT_EXTENSION)
            self.closed_index_files = _get_by_extension(all_files, CLOSED_INDEX_EXTENSION)
        else:
            raise ValueError(f"Path doesn't appear to be a directory: {directory_path}")

    def write_to_index(self, document_id, text):
        if not self.open_index_file:
            self._get_new_file(OPEN_INDEX_EXTENSION)
            self.open_index = Index()
        with self.open_index as open_index:
            open_index.write(document_id, text)

    def commit(self):
        self.open_index.commit()
        _write_data_to_file(self.open_index_file, self.open_index)

    def append_document(self, document_id, document):
        # TODO - call this when committing, and flush to rest of documents
        if not self.open_document_file:
            self.open_document_file = self._get_new_file(OPEN_DOCUMENT_EXTENSION)
        _write_data_to_file(self.open_document_file, {document_id: document})
    
    def _get_new_file(self, extension):
        # TODO - Check if it already exists
        file_name = uuid.uuid4().hex[:6]
        complete_path = f"{self.directory_path}/{file_name}{extension}"
        with open(complete_path, "wb+"): pass
        return complete_path
        
    

def _get_files_in_path(directory_path):
    return [
        file for file in listdir(directory_path)
        if path.isfile(
            path.join(directory_path, file)
        )
    ]


def _get_by_extension(files, extension):
    return [
        file 
        for file in files
        if file.endswith(extension)
    ]

def _get_open_file(open_files):
    if len(open_files) > 1:
        raise ValueError("Corrupt Index! There appears to be more than 1 open file of the same type.")
    if len(open_files) == 1:
        return open_files[0]
    return None

    
def _write_data_to_file(filename, data):
    # TODO - Should go in the IndexWriter?
    data_as_bytes = io.BytesIO()
    pickle.dump(data, data_as_bytes)
    
    compressed_bytes = zlib.compress(data_as_bytes.getbuffer())
    with open(filename, "ab") as open_document_file:
        open_document_file.write(compressed_bytes)
        open_document_file.write(linesep.encode())

"""
In [64]: def file2dict(filename):
    ...:     with open(filename, 'rb') as fd:
    ...:         for zbytes in fd:
    ...:             bytes = zlib.decompress(zbytes)
    ...:             data = pickle.loads(bytes)
    ...:             print(data)
    ...:

In [65]: file2dict(df)
{'132UDI5489FDJHI': 'This is a string of text wow!'}
{'14378UHHJWD823J': "ANother string? omg i'm so lucky!"}
"""