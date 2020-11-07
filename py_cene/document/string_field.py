from py_cene.document.field import Field


class StringField(Field):
    def _process(self):
        if not isinstance(self.value, str):
            # log 
            self.value = str(self.value)
        if len(self.value.split()) > 1:
            raise ValueError("StringField can not be multi unit, i.e. separated")