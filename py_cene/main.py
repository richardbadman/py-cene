#!/usr/bin/env python

from py_cene.analyser import format_text
from py_cene.directory import DirectoryFactory


def main():
    documents = {
        1: "Winter is coming",
        2: "I hate winter coats!",
        3: "Christmas is, early this year"
    }

    directory_factory = DirectoryFactory()
    cache_directory = directory_factory.create("CACHE")
    cache_directory.create_new_index("test")
    
    cache_directory.write_to_index("test", documents)
    cache_directory.commit_index("test")
    
    results = cache_directory.search("winter")
    print(results)

if __name__ == "__main__":
    main()