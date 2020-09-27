import time

from collections import OrderedDict


class Segment:
    # TODO
    # [ ] Convert this to a bitmap
    def __init__(self, segment_prefix):
        self.dictionary = OrderedDict()
        self.name = segment_prefix
        self.comitted = False

    def __repr__(self):
        return f"Segment({self.name})"

    def __str__(self):
        return f"{self.name}"

    def write(self, document_id, text):
        if self.comitted:
            raise ValueError("Trying to write to already committed segment")
        for word in text:
            if word in self.dictionary.keys():
                self.dictionary[word]["frequency"] += 1
                self.dictionary[word]["documents"].append(document_id)
            else:
                self.dictionary[word] = {
                    "frequency": 1,
                    "documents": [document_id]
                }
        print(f"Written document id {document_id}")
        
    def commit(self):
        hash_id = str(hash(time.time()))[:6]
        self.name = f"{self.name}_{hash_id}"
        print(f"Commiting segment: {self.name}")
        self.comitted = True

    # TODO - Not actually have this
    def get(self):
        return self.dictionary