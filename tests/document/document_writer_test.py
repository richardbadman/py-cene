from pytest import raises

from py_cene.analyser import StandardAnalyser
from py_cene.document.document import Document
from py_cene.document.document_writer import DocumentWriter
from py_cene.document.string_field import StringField
from py_cene.document.text_field import TextField


STANDARD_ANALYSER = StandardAnalyser()
INDEXED_STRING_FIELD_NOT_STORED = StringField("id", "1324")
INDEXED_TEXT_FIELD_NOT_STORED = TextField("text", "A simple string")
INDEXED_TEXT_FIELD_STORED = TextField("text", "A simple string", True)
NOT_INDEXED_TEXT_FIELD_STORED = TextField("email", "testing@test.com", index=False)


def test_when_writing_document_then_segments_are_populated():
    document = Document()
    document.add(INDEXED_STRING_FIELD_NOT_STORED)
    document.add(INDEXED_TEXT_FIELD_STORED)
    
    document_writer = DocumentWriter(document, STANDARD_ANALYSER)
    document_writer.write_document()

    assert len(document_writer.index_segment.dictionary) > 0
    assert len(document_writer.data_segment.dictionary) > 0

    
def test_when_writing_document_with_only_indexed_fields_then_data_segment_is_empty():
    document = Document()
    document.add(INDEXED_STRING_FIELD_NOT_STORED)
    document.add(INDEXED_TEXT_FIELD_NOT_STORED)
    
    document_writer = DocumentWriter(document, STANDARD_ANALYSER)
    document_writer.write_document()
    
    assert len(document_writer.index_segment.dictionary) > 0
    assert len(document_writer.data_segment.dictionary) == 0


def test_when_attempting_to_write_document_with_no_indexed_fields_then_exception_is_met():
    document = Document()
    document_writer = DocumentWriter(document, STANDARD_ANALYSER)
    with raises(ValueError):
        document_writer.write_document()