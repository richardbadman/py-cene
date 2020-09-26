from src.index.segment import Segment

def test_word_frequency_expected():
    documents = {
        1: "winter is coming",
        2: "I hate winter coats"
    }
    segment = Segment("test")
    for document_id, document in documents.items():
        segment.write(document, document_id)
        
    data = segment.get()
    expected_frequency_for_winter = 2
    actual_frequency_for_winter = data["winter"]["frequency"]

    assert expected_frequency_for_winter == actual_frequency_for_winter