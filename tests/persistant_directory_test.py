import os
import tempfile
import unittest

from pytest import raises
from shutil import rmtree

from py_cene.analyser import format_text
from py_cene.directory import DirectoryFactory


DOCUMENT = "A sample text."
DIRECTORY_FACTORY = DirectoryFactory()
TEMP_DIRECTORY = f"{tempfile.gettempdir()}/py_cene_testing"
TEXT = format_text(DOCUMENT)

def clean_up():
    os.remove(TEMP_DIRECTORY)

class PersistantDirectoryTest(unittest.TestCase):

    def setUp(self):
        os.mkdir(TEMP_DIRECTORY)
        self.persistant_directory = DIRECTORY_FACTORY.create("PERSISTANT")
        self.persistant_directory.get_directory(TEMP_DIRECTORY)
        
    def tearDown(self):
        rmtree(TEMP_DIRECTORY)

    def test_writing_to_index(self):
        self.persistant_directory.write_to_index(1, TEXT) 

    def test_appending_documents(self):
        self.persistant_directory.append_document(1, DOCUMENT)
        
    def test_when_commiting_index_with_no_data_then_exception_is_met(self):
        with raises(ValueError):
            self.persistant_directory.commit()

    def test_searching_index(self):
        self.persistant_directory.write_to_index(1, TEXT)
        self.persistant_directory.commit()

        expected_results = {1: 1}
        actual_results = self.persistant_directory.search_index("text")
        assert expected_results == actual_results

    def test_getting_documents(self):
        self.persistant_directory.write_to_index(1, TEXT)
        self.persistant_directory.append_document(1, DOCUMENT)
        self.persistant_directory.commit()

        expected_results = ["A sample text."]
        actual_results = self.persistant_directory.get_documents([1])
        assert expected_results == actual_results

    def test_when_creating_entirely_new_persistant_directory_no_data_is_there(self):
        expected_results = dict()
        actual_results = self.persistant_directory.search_index("term")
        assert expected_results == actual_results

    def test_when_opening_persistant_directory_that_already_exists_on_disk_then_data_is_there(self):
        self.persistant_directory.write_to_index(1, TEXT)
        self.persistant_directory.append_document(1, DOCUMENT)
        self.persistant_directory.commit()

        self.persistant_directory = None
        self.persistant_directory = DIRECTORY_FACTORY.create("PERSISTANT")
        self.persistant_directory.get_directory(TEMP_DIRECTORY)
        
        expected_results = {1: 1}
        actual_results = self.persistant_directory.search_index("text")
        assert expected_results == actual_results

    def test_writing_multiple_documents_and_then_checking_they_persist(self):
        documents = {
            1: "A sample text.",
            2: "Another text line"
        }
        
        for document_id, document in documents.items():
            text = format_text(document)
            self.persistant_directory.write_to_index(document_id, text)
            self.persistant_directory.append_document(1, document)
        self.persistant_directory.commit()

        self.persistant_directory = None
        self.persistant_directory = DIRECTORY_FACTORY.create("PERSISTANT")
        self.persistant_directory.get_directory(TEMP_DIRECTORY)
        
        expected_results = {1: 1, 2: 1}
        actual_results = self.persistant_directory.search_index("text")
        assert expected_results == actual_results