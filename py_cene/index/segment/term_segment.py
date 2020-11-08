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

    def merge(self, other):
        self.dictionary = {
            key: _merge(
                self.dictionary.get(key),
                other.dictionary.get(key)
            )
            for key in set(self.dictionary).union(other.dictionary)
        }


def _merge(this, other):
    if this is None:
        return other
    elif other is None:
        return this
    else:
        return {**this, **other}