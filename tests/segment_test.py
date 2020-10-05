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
    # TODO
    pass

def test_when_segment_committed_cannot_be_written_to_again():
    segment = Segment()
    for document_id, document in DOCUMENTS.items():
        text = format_text(document)
        segment.write(document_id, text)
    segment.commit()
    with raises(ValueError):
        segment.write(3, "this will fail")