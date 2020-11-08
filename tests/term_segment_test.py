from py_cene.index.term_segment import TermSegment


DOCUMENT_ID = "1UA"
DOCUMENT = {
    "content": ["simple", "string"]
}


def test_when_writing_data_then_segment_is_populated():
    segment = TermSegment()
    segment.write(DOCUMENT_ID, content=DOCUMENT)
    
    assert len(segment.dictionary) > 0