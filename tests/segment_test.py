from pytest import raises

from py_cene.analyser import format_text
from py_cene.index.segment import Segment


DOCUMENTS = {
    1: "winter is coming",
    2: "I hate winter coats"
}


def test_word_frequency():
    segment = Segment()
    for document_id, document in DOCUMENTS.items():
        text = format_text(document)
        segment.write(document_id, text)
        
    data = segment.get()
    expected_frequency_for_winter = 2
    actual_frequency_for_winter = data["winter"]["frequency"]

    assert expected_frequency_for_winter == actual_frequency_for_winter

def test_document_mapping():
    segment = Segment()
    for document_id, document in DOCUMENTS.items():
        text = format_text(document)
        segment.write(document_id, text)
        
    results = segment.search("winter")
    expected_document_ids = [1, 2]
    actual_document_ids = [
        document_id
        for term, data in results.items()
        for document_id in data["documents"]
    ]
    
    assert expected_document_ids == actual_document_ids

def test_search_term_returning_no_results():
    segment = Segment()
    results = segment.search("empty")
    assert results == dict()

def test_when_segment_committed_cannot_be_written_to_again():
    segment = Segment()
    for document_id, document in DOCUMENTS.items():
        text = format_text(document)
        segment.write(document_id, text)
    segment.commit()
    with raises(ValueError):
        segment.write(3, "this will fail")