import uuid 

from unittest.mock import patch

from py_cene.directory import DirectoryFactory
from py_cene.index import IndexWriter, IndexSearcher

DIRECTORY_FACTORY = DirectoryFactory()
DOCUMENTS = ["A sample text.", "Another sample line!"]
TEST_UUID = 0
def mock_uuid():
    global TEST_UUID
    TEST_UUID += 1
    return uuid.UUID(int=TEST_UUID)

def test_when_searching_term_in_both_documents_then_both_documents_are_returned():
    cache_directory = DIRECTORY_FACTORY.create("CACHE")
    index_writer = IndexWriter(cache_directory)
    index_searcher = IndexSearcher(cache_directory)
    
    for document in DOCUMENTS:
        index_writer.add_document(document)
    index_writer.commit()
    
    expected_results = ["A sample text.", "Another sample line!"]
    actual_results = index_searcher.search("sample")

    assert expected_results == actual_results

def test_when_searching_term_in_only_one_document_then_only_that_document_is_returned():
    cache_directory = DIRECTORY_FACTORY.create("CACHE")
    index_writer = IndexWriter(cache_directory)
    index_searcher = IndexSearcher(cache_directory)
    
    for document in DOCUMENTS:
        index_writer.add_document(document)
    index_writer.commit()

    expected_results = ["A sample text."]
    actual_results = index_searcher.search("text")
    
    assert expected_results == actual_results
    
def test_when_searching_term_in_neither_documents_then_no_docuemtns_are_returned():
    cache_directory = DIRECTORY_FACTORY.create("CACHE")
    index_writer = IndexWriter(cache_directory)
    index_searcher = IndexSearcher(cache_directory)
    
    for document in DOCUMENTS:
        index_writer.add_document(document)
    index_writer.commit()

    expected_results = []
    actual_results = index_searcher.search("empty")
    
    assert expected_results == actual_results

def test_when_searching_term_on_index_with_no_data_then_no_documents_are_returned():
    cache_directory = DIRECTORY_FACTORY.create("CACHE")
    index_searcher = IndexSearcher(cache_directory)
    
    expected_results = []
    actual_results = index_searcher.search("empty")

    assert expected_results == actual_results