from py_cene.document.field import Field


class Document:
    def __init__(self):
        self.fields = []
    
    def add(self, field):
        if not isinstance(field, Field):
            raise ValueError("Field was not a field type")
        self.fields.append(field)

    def validate(self):
        return any([field.index for field in self.fields])

    def __iter__(self):
        for n in range(len(self.fields)):
            yield self.fields[n]