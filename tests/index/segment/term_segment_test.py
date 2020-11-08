from py_cene.index.segment.term_segment import TermSegment


DOCUMENTS = [
    {
        "id": "1UA",
        "data": ["simple", "string"]
    },
    {
        "id": "1XV",
        "data": ["another", "string"]
    }
]


def test_when_writing_data_then_segment_is_populated():
    segment = TermSegment()
    segment.write(DOCUMENTS[1]["id"], content=DOCUMENTS[1]["data"])
    
    assert len(segment.dictionary) > 0

    
def test_when_writing_data_check_contents_of_segment_are_correct():
    expected_result = {
        "simple": {
            "1UA": 1
        },
        "string": {
            "1UA": 1
        }
    }
    segment = TermSegment()
    segment.write(DOCUMENTS[0]["id"], content=DOCUMENTS[0]["data"])
    
    actual_result = segment.dictionary
    assert expected_result == actual_result

    
def test_when_writing_more_than_one_document_then_check_the_contents_of_the_segment():
    expected_result = {
        "another": {
            "1XV": 1
        },
        "simple": {
            "1UA": 1
        },
        "string": {
            "1UA": 1,
            "1XV": 1
        }
    }
    segment = TermSegment()
    for info in DOCUMENTS:
        segment.write(info["id"], content=info["data"])
        
    actual_result = segment.dictionary
    assert expected_result == actual_result

    
def test_when_merging_two_term_segments_with_no_duplicates_verify_output():
    expected_result = {
        "simple": {
            "IXA": 1
        },
        "string": {
            "IXA": 1
        },
        "another": {
            "XBA": 1
        },
        "word": {
            "XBA": 1
        }
    }
    
    id_one = "IXA"
    data_one = ["simple", "string"]
    id_two = "XBA"
    data_two = ["another", "word"]
    
    segment_one = TermSegment()
    segment_two = TermSegment()
    
    segment_one.write(id_one, content=data_one)
    segment_two.write(id_two, content=data_two)
    
    segment_one.merge(segment_two)
    actual_result = segment_one.dictionary
    
    assert expected_result == actual_result

    
def test_when_merging_two_term_segments_with_some_duplicates_verify_contents():
    expected_result = {
        "simple": {
            "IXA": 1
        },
        "string": {
            "IXA": 1,
            "XBA": 1
        },
        "another": {
            "XBA": 1
        }
    }
    
    id_one = "IXA"
    data_one = ["simple", "string"]
    id_two = "XBA"
    data_two = ["another", "string"]
    
    segment_one = TermSegment()
    segment_two = TermSegment()
    
    segment_one.write(id_one, content=data_one)
    segment_two.write(id_two, content=data_two)
    
    segment_one.merge(segment_two)
    actual_result = segment_one.dictionary
    
    assert expected_result == actual_result