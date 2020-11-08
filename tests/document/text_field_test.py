from py_cene.document.text_field import TextField


def test_when_creating_a_valid_text_field_no_exception_is_made():
    TextField(
        "test",
        "this-wont-break"
    )