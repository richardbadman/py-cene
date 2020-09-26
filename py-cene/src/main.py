#!/usr/bin/env python

from index.segment import Segment


def main():
    segment = Segment("seg")
    documents = {
        1: "Winter is coming",
        2: "I hate winter coats!",
        3: "Christmas is, early this year"
    }
    
    for document_id, document in documents.items():
        segment.write(document, document_id)

    print(segment.get())


if __name__ == "__main__":
    main()