from py_cene.document.field import Field


class TextField(Field):
    def _process(self):
        if not isinstance(self.value, str):
            # log
            self.value = str(self.value)