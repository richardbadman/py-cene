from pytest import raises

from py_cene.analyser import format_text
from py_cene.index.index import Index


TEXT = {
    1: "This is a line of text",
    2: "This is another line of text",
    3: "A completely different type of message",
    4: "Some more characters for this test",
    5: "This passage is not the same as the others"
}

def test_when_soft_committing_three_segments_exist():
    index = Index("testing_index")
    with index as open_index:
        for document_id, document in TEXT.items():
            text = format_text(document)
            open_index.write(document_id, text)
            open_index.soft_commit()
            
    actual_number_of_segments = len(index.get_segments())
    expected_number_of_segments = 5
    
    assert actual_number_of_segments == expected_number_of_segments

def test_when_soft_committing_three_segments_all_prefixes_are_the_same():
    index = Index("testing_index")
    with index as open_index:
        for document_id, document in TEXT.items():
            text = format_text(document)
            open_index.write(document_id, text)
            open_index.soft_commit()
            
    segments_prefixes = [
        str(segment).split("_")[0]
        for segment in index.get_segments() 
    ]
    assert all(segments_prefixes)

def test_when_hard_committing_segment_prefixes_differ():
    index = Index("testing_index")
    with index as open_index:
        for document_id, document in TEXT.items():
            text = format_text(document)
            open_index.write(document_id, text)
            if document_id < 3:
                open_index.soft_commit()
            else:
                open_index.hard_commit()
            
    segments_prefixes = {
        str(segment).split("_")[0]
        for segment in index.get_segments()
    }
    assert len(segments_prefixes) > 1

def test_when_hard_committing_past_segment_prefix_limit_exception_is_throw():
    index = Index("testing_index")
    with raises(ValueError):
        with index as open_index:
            for document_id, document in TEXT.items():
                open_index.write(document_id, document)
                open_index.hard_commit()