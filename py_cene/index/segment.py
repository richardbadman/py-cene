import time

from collections import OrderedDict


class Segment:
    # TODO
    # [ ] Convert this to a bitmap
    # [ ] support search
    def __init__(self):
        self.dictionary = OrderedDict()
        self.name = None
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
        hash_id = str(hash(time.time()))[:8]
        self.name = f"{hash_id}"
        print(f"Commiting segment: {self.name}")
        self.comitted = True

    # TODO - Not actually have this
    def get(self):
        return self.dictionary

    def search(self, term):
        if term in self.dictionary:
            return {
                term: self.dictionary[term]
            }
        return dict()