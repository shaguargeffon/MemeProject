"""Parse different kinds of files according to the given classes.

The Ingestor class supplies a `parse` function which is a class method.
It receives a filename with string format and checks if the defined
elements in ingestors are compatible to the given filename.
If it is compatible, then it will call the corresponding class method
parse to return a list which contains a set of Quote Models.
"""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """An ingestor to check format of given filename and parse it."""

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Check format of given filename and parse it.

        for instance the DogQuotesTXT.txt is like this:
        To bork or not to bork - Bork
        He who smelt it... - Stinky

        It will return the list [QuoteModel('To bork or not to bork', 'Bork'),
        QuoteModel('He who smelt it...', 'Stinky')]

        :param path: path of file and file name, it shall be a string.
        :return: A list contains QuoteModel objects.
        """
        for quotes in cls.ingestors:
            if quotes.can_ingest(path):
                return quotes.parse(path)
