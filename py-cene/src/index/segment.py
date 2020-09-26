import re
import time

from collections import OrderedDict

from stopwords import STOPWORDS
"""
Brain dump

Example text and output

1. Winter is coming
2. I hate winter coats
3. Christmas is early this year

+-----------+-----------+----------+
|   Term    | Frequency | Document |
+-----------+-----------+----------+
| christmas |         1 |        3 |
| coats     |         1 |        2 |
| coming    |         1 |        1 |
| early     |         1 |        3 |
| hate      |         1 |        2 |
| winter    |         2 |     1, 2 |
| year      |         1 |        3 |
+-----------+-----------+----------+

---

If we want want to search for say co* we can do a binary look up for that and disect to the co part of the dictionary keys
but we can worry about this later

"""

PUNCTIONATION_REGEX = r"[^\w\s]"

class Segment:
    def __init__(self, segment_prefix):
        self.dictionary = OrderedDict()
        self.name = segment_prefix

    def write(self, text, document_id):
        formatted_text = _format_text(text)
        for word in formatted_text:
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
        # TODO - "Close" segment
        hash_id = str(hash(time.time()))[:6]
        self.name = f"{self.name}_{hash_id}"

    # TODO - Not actually have this
    def get(self):
        return self.dictionary


def _format_text(text):
    text_lower = text.lower().rstrip()
    text_no_punctuation = re.sub(PUNCTIONATION_REGEX, "", text_lower)
    words = text_no_punctuation.split()
    return [
        word for word in words 
        if word not in STOPWORDS
    ]