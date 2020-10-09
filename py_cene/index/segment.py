import time

from collections import OrderedDict


class Segment:
    # TODO
    # [ ] Convert this to a bitmap
    # [x] support search
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
            if word in self.dictionary:
                if document_id in self.dictionary[word]:
                    self.dictionary[word][document_id] += 1
                else:
                    self.dictionary[word][document_id] = 1
            else:
                self.dictionary[word] = {document_id: 1}
        print(f"Written document id {document_id}")
        
    def commit(self):
        hash_id = str(hash(time.time()))[:8]
        self.name = f"{hash_id}"
        print(f"Commiting segment: {self.name}")
        self.comitted = True

    def search(self, term):
        if term in self.dictionary:
            return self.dictionary[term]
        return dict()