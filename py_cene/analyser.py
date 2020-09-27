import re

from py_cene.stopwords import STOPWORDS


PUNCTUATION_REGEX = r"[^\w\s]"

def format_text(text):
    text_to_lower = text.lower().rstrip()
    text_with_no_punctuation = re.sub(PUNCTUATION_REGEX, "", text_to_lower)
    words = text_with_no_punctuation.split()
    return [
        word for word in words if words
        if word not in STOPWORDS
    ]