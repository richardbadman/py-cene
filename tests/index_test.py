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

def test_search_term_over_a_number_of_segments():
    index = Index("testing_index")
    results = dict()
    with index as open_index:
        for document_id, document in DOCUMENTS.items():
            text = format_text(document)
            open_index.write(document_id, text)
            open_index.commit()
            
        results = index.search("line")
        
    expected_document_ids = [1, 2]
    actual_document_ids = list(results["line"].keys())
    
    assert sorted(expected_document_ids) == sorted(actual_document_ids)

def test_search_term_on_empty_index_returns_no_results():
    index = Index("testing_index")
    with index as open_index:
        results = open_index.search("empty")
    
        assert results == dict()

def test_search_term_on_index_with_no_matches():
    index = Index("testing_index")
    with index as open_index:
        for document_id, document in DOCUMENTS.items():
            text = format_text(document)
            open_index.write(document_id, text)
            open_index.commit()
            
        results = open_index.search("empty")
        assert results == dict()

def test_writing_to_index_thats_not_open_raises_exception():
    index = Index("testing_index")
    with raises(ValueError):
        for document_id, document in DOCUMENTS.items():
            index.write(document_id, document)

def test_searching_an_index_thats_not_open_raises_exception():
    index = Index("testing_index")
    with raises(ValueError):
        for document_id, document in DOCUMENTS.items():
            index.search("fail")

def test_when_writing_and_not_committing_then_data_isnt_searchable():
    index = Index("testing_index")
    for document_id, document in DOCUMENTS.items():
        with index as open_index:
            open_index.write(document_id, document)

            results = open_index.search("empty")
            assert results == dict()