"""A python module defines a class DocxIngestor."""

from typing import List
import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """A DocxIngestor object which can parse csv file.

    The class DocxIngestor is inherited from IngestorInterface.
    It supplies a class method parse to parse docx file.
    Then the method uses the parsed information to get a list
    contains QuoteModel objects and return the list.
    """

    supported_file_type = ['docx']

    @classmethod
    def parse(cls, filename: str) -> List[QuoteModel]:
        """Read a given docx file, build a list that \
        contains QuoteModel objects.

        :param filename: path of file and file name, it shall be a string.
        :return: a list contains QuoteModel objects.
        """
        if not cls.can_ingest(filename):
            raise Exception('cannot ingest Docx file.')
        parse_list = list()
        docx_handle = docx.Document(filename)

        for content in docx_handle.paragraphs:
            if content.text != "":
                text = content.text.split('-')
                body = text[0].strip().strip('"')
                author = text[1].strip()
                qm = QuoteModel(body, author)
                parse_list.append(qm)

        return parse_list
