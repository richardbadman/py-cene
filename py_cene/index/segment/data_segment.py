from py_cene.index.segment.segment import Segment


class DataSegment(Segment):
    def write(self, document_id, **kwargs):
        key = kwargs["field_key"]
        if document_id in self.dictionary:
            self.dictionary[document_id][key] = kwargs["content"]
        else:
            self.dictionary[document_id] = {key: kwargs["content"]}

    def combine(self, other):
        pass