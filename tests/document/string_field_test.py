from pytest import raises

from py_cene.document.string_field import StringField


def test_when_creating_a_valid_string_field_no_exception_is_made():
    StringField(
        "test",
        "this-wont-break"
    )
    
    
def test_when_creating_a_string_field_with_separators_then_exception_is_made():
    with raises(ValueError):
        StringField(
            "test",
            "this will break"
        )
        

def test_when_creating_a_string_field_that_isnt_a_string_then_value_is_now_a_string():
    string_field = StringField(
        "test",
        100
    )
    assert "100" == string_field.value
    