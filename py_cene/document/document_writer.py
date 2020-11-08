"""
Every thread processes data in its own independent DocumentsWriterPerThread space,
including tokenizing, relevance scoring and indexing

A flush is the process of making in-memory buffers in DWPT into data-persistent
files. A flush is automatically triggered after a new document is added based on 
FlushPolicy, and a flush can also be manually triggered using IndexWriter's 
flush interface.

Every DWPT is flushed into a segment file. A segment file is not searchable 
after a flush has completed, and is only searchable after a commit, when all 
flushed documents become searchable.

--
So, make each document writer return a segment file, and then a commit uses theses
in memory segment files to then write a new segment file to disk!

Some functions here will only be callable if its being indexed, 
and requires tokenisation
"""
import uuid

from py_cene.document.string_field import StringField
from py_cene.index.segment.data_segment import DataSegment
from py_cene.index.segment.term_segment import TermSegment


class DocumentWriter:
    # TODO - Make extend the thread class
    def __init__(self, document, analyser):
        self.document = document
        self.analyser = analyser
        self.index_segment = TermSegment()
        self.data_segment = DataSegment()
        self.id = uuid.uuid4().hex
        
    def write_document(self):
        if not self.document.validate():
            raise ValueError("No fields for document are being index, please add one")
        internal_id_field = StringField("_id", self.id, store=True, index=False)
        self.document.add(internal_id_field)
        for field in self.document:
            self._process(field)
                
    def _process(self, field):
        if field.index:
            self._index_field(field)
        if field.store:
            self._store_field(field)
        
    def _index_field(self, field):
        tokenised_data = self.analyser.format_text(field.value)
        self.index_segment.write(
            self.id,
            content=tokenised_data
        )
    
    def _store_field(self, field):
        self.data_segment.write(
            self.id,
            field_key=field.name,
            content=field.value
        )
        
    def flush(self):
        # TODO - basically make this thread stop
        pass