from py_cene.index.segment.segment import Segment


class TermSegment(Segment):
    def write(self, document_id, **kwargs):
        print(kwargs["content"])
        for word in kwargs["content"]:
            if word in self.dictionary:
                if document_id in self.dictionary[word]:
                    self.dictionary[word][document_id] += 1
                else:
                    self.dictionary[word][document_id] = 1
            else:
                self.dictionary[word] = {document_id: 1}

    def combine(self, other):
        pass
       