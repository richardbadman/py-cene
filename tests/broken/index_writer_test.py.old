from pytest import raises

from py_cene.directory import DirectoryFactory
from py_cene.index import IndexWriter


DIRECTORY_FACTORY = DirectoryFactory()
DOCUMENTS = ["A sample text.", "Another sample line!"]

def test_writing_to_index():
    cache_directory = DIRECTORY_FACTORY.create("CACHE")
    index_writer = IndexWriter(cache_directory)
    for document in DOCUMENTS:
        index_writer.add_document(document)
    index_writer.commit()

def test_when_indexing_two_documents_then_ids_differ():
    cache_directory = DIRECTORY_FACTORY.create("CACHE")
    index_writer = IndexWriter(cache_directory)
    for document in DOCUMENTS:
        index_writer.add_document(document)
    index_writer.commit()

    document_ids = list(
        cache_directory.search_index("sample").keys()
    )
    document_id_one = document_ids[0]
    document_id_two = document_ids[1]
    
    assert not document_id_one == document_id_two

def test_when_commiting_to_empty_index_exception_is_thrown():
    cache_directory = DIRECTORY_FACTORY.create("CACHE")
    index_writer = IndexWriter(cache_directory)
    with raises(ValueError):
        index_writer.commit()