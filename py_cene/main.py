#!/usr/bin/env python

from py_cene.analyser import format_text
from py_cene.directory import DirectoryFactory
from py_cene.index import (
    IndexWriter,
    IndexSearcher
)


def main():
    documents = [
        "I've just hung out my washing, it should dry by tomorrow",
        "I'm really enjoying doing this project and learning more about lucene",
        "Lucene has been around for a long long time"
    ]
    
    directory_factory = DirectoryFactory()
    cache_directory = directory_factory.create("CACHE")
    index_writer = IndexWriter(cache_directory)
    index_searcher = IndexSearcher(cache_directory)
    
    for document in documents:
        index_writer.add_document(document)
    index_writer.commit()

    documents = index_searcher.search("lucene")
    print(documents)
    

if __name__ == "__main__":
    main()