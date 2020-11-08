import unittest

from pytest import raises

from py_cene.analyser import format_text
from py_cene.directory import DirectoryFactory


DOCUMENT = "A sample text."
DIRECTORY_FACTORY = DirectoryFactory()
TEXT = format_text(DOCUMENT)

class CacheDirectoryTest(unittest.TestCase):
    def setUp(self):
        self.cache_directory = DIRECTORY_FACTORY.create("CACHE")

    def test_when_creating_new_cache_directory_no_documents_are_there(self):
        assert self.cache_directory.documents == dict()
    
    def test_writing_to_index(self):
        self.cache_directory.write_to_index(1, TEXT)

    def test_append_document(self):
        self.cache_directory.append_document(1, DOCUMENT)
    
    def test_when_commiting_index_with_no_data_then_exception_is_met(self):
        with raises(ValueError):
            self.cache_directory.commit()
    
    def test_searching_index(self):
        self.cache_directory.write_to_index(1, TEXT)
        self.cache_directory.commit()
        
        expected_results = {1: 1}
        actual_results = self.cache_directory.search_index("sample")
        assert expected_results == actual_results
    
    def test_getting_documents(self):
        self.cache_directory.write_to_index(1, TEXT)
        self.cache_directory.commit()
        self.cache_directory.append_document(1, DOCUMENT)
        
        expected_results = ["A sample text."]
        actual_results = self.cache_directory.get_documents([1])
        assert expected_results == actual_results