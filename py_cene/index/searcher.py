import zlib


class IndexSearcher:
    # TODO
    # [ ] - give logic to directory to make it bound to this class
    def __init__(self, directory):
        self.directory = directory

    def search(self, term):
        results = _sort_results(
            self.directory.search_index(term)
        )
        document_ids = results.keys()
        compressed_documents = self.directory.get_documents(document_ids)
        return [
            zlib.decompress(document).decode()
            for document in compressed_documents
        ]
        

def _sort_results(results):
    return {
        document_id: frequency 
        for document_id, frequency in sorted(
            results.items(),
            key=lambda item: item[1],
            reverse=True)
    }