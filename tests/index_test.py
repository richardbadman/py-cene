from pytest import raises

from py_cene.analyser import format_text
from py_cene.index.index import Index


DOCUMENTS = {
    1: "This is a line of text",
    2: "This is another line of text",
    3: "A completely different type of message"
}

def test_when_soft_committing_three_segments_exist():
    index = Index("testing_index")
    with index as open_index:
        for document_id, document in DOCUMENTS.items():
            text = format_text(document)
            open_index.write(document_id, text)
            open_index.commit()
            
    actual_number_of_segments = len(index.get_segments())
    expected_number_of_segments = 3
    
    assert actual_number_of_segments == expected_number_of_segments

def test_when_trying_to_open_index_when_already_open_exception_is_thrown():
    index = Index("testing_index")
    duplicate = index
    with index as open_index: # pylint: disable=unused-variable
        with raises(ValueError):
            with duplicate as should_raise:  # pylint: disable=unused-variable
                assert False