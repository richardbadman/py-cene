from py_cene.index.segment.data_segment import DataSegment


DOCUMENTS = [
    {
        "id": "1UA",
        "field_key": "text",
        "content": "A simple string"
    },
    {
        "id": "1XV",
        "field_key": "text",
        "content": "another string!"
    }
]
def test_when_writing_data_then_segment_is_populated():
    segment = DataSegment()
    segment.write(
        DOCUMENTS[0]["id"],
        field_key=DOCUMENTS[0]["field_key"],
        content=DOCUMENTS[0]["content"]
    )
    
    assert len(segment.dictionary) > 0


def test_when_writing_data_check_contents_of_segment_are_correct():
    expected_results = {
        "1UA": {
            "text": "A simple string"
        }
    }
    segment = DataSegment()
    segment.write(
        DOCUMENTS[0]["id"],
        field_key=DOCUMENTS[0]["field_key"],
        content=DOCUMENTS[0]["content"]
    )
    
    actual_result = segment.dictionary
    assert expected_results == actual_result


def test_when_writing_more_than_one_document_then_check_the_contents_of_the_segment():
    expected_results = {
        "1UA": {
            "text": "A simple string"
        },
        "1XV": {
            "text": "another string!"
        }
    }
    segment = DataSegment()
    for info in DOCUMENTS:
        segment.write(
            info["id"],
            field_key=info["field_key"],
            content=info["content"]
        )

    actual_result = segment.dictionary
    assert expected_results == actual_result

    
def test_when_merging_two_data_segments_then_verify_contents():
    expected_results = {
        "IXA": {
            "test": "A simple string"
        },
        "XBA": {
            "info": "Another string!"
        }
    }
    id_one = "IXA"
    key_one = "test"
    data_one = "A simple string"
    id_two = "XBA"
    key_two = "info"
    data_two = "Another string!"
    
    segment_one = DataSegment()
    segment_two = DataSegment()
    
    segment_one.write(
        id_one, 
        field_key=key_one,
        content=data_one
    )
    segment_two.write(
        id_two,
        field_key=key_two,
        content=data_two
    ) 
    
    segment_one.merge(segment_two)
    actual_result = segment_one.dictionary
    
    assert expected_results == actual_result