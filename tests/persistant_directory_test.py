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
        
    def tearDown(self):
        rmtree(TEMP_DIRECTORY)

    def test_writing_to_index(self):
        persistant_directory = DIRECTORY_FACTORY.create("PERSISTANT")
        persistant_directory.get_directory(TEMP_DIRECTORY)
        
        persistant_directory.write_to_index(1, TEXT) 

    def test_appending_documents(self):
        persistant_directory = DIRECTORY_FACTORY.create("PERSISTANT")
        persistant_directory.get_directory(TEMP_DIRECTORY)
        
        persistant_directory.append_document(1, DOCUMENT)
        
    def test_when_commiting_index_with_no_data_then_exception_is_met(self):
        # TODO
        pass
        # persistant_directory = DIRECTORY_FACTORY.create("PERSISTANT")
        # persistant_directory.get_directory(TEMP_DIRECTORY)

        # with raises(ValueError):
        #     persistant_directory.commit()

    def test_searching_index(self):
        pass

    def test_getting_documents(self):
        pass

    def test_when_creating_entirely_new_persistant_directory_no_data_is_there(self):
        pass

    def test_when_opening_persistant_directory_that_already_exists_on_disk_data_is_there(self):
        pass