from pytest import raises

from py_cene.document.document import Document
from py_cene.document.string_field import StringField
from py_cene.document.text_field import TextField


def test_when_adding_a_document_and_supplying_invalid_field_exception_is_met():
    document = Document()
    with raises(ValueError):
        document.add(1)
        
        
def test_when_adding_a_field_check_contents_are_correct():
    expected_result = "test"
    string_field = StringField("test", "test")
    document = Document()
    
    document.add(string_field)
    for field in document:
        assert field.value == expected_result
        
        
def test_when_adding_multiple_fields_then_values_differ():
    expected_result = [
        "test",
        "A simple string"
    ]
    string_field = StringField("test", "test")
    text_field = TextField("test", "A simple string")
    document = Document()
    
    document.add(string_field)
    document.add(text_field)
    
    actual_result = [field.value for field in document]
    assert expected_result == actual_result


def test_when_adding_fields_and_indexing_defaults_to_true_then_validate_returns_true():
    expected_result = True
    string_field = StringField("test", "test")
    text_field = TextField("test", "A simple string")
    document = Document()
    
    document.add(string_field)
    document.add(text_field)
    
    actual_result = document.validate()
    assert expected_result == actual_result
    
    
def test_when_adding_fields_and_not_indexing_then_validate_returns_false():
    expected_result = False
    string_field = StringField("test", "test", index=False)
    text_field = TextField("test", "A simple string", index=False)
    document = Document()
    
    document.add(string_field)
    document.add(text_field)
    
    actual_result = document.validate()
    assert expected_result == actual_result