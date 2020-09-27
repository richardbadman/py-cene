#!/usr/bin/env python

from py_cene.analyser import format_text
from py_cene.index.index import Index


def main():
    index = Index("test")
    documents = {
        1: "Winter is coming",
        2: "I hate winter coats!",
        3: "Christmas is, early this year"
    }
    
    with index as open_index:
        for document_id, document in documents.items():
            text = format_text(document)
            open_index.write(document_id, text)
        open_index.hard_commit()

    print(index.get_segments())


if __name__ == "__main__":
    main()