"""A python module defines a class PDFIngestor."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import subprocess
import os


class PDFIngestor(IngestorInterface):
    """A PDFIngestor object which can parse pdf file.

    The class PDFIngestor is inherited from IngestorInterface.
    It supplies a class method parse to parse pdf file.
    Then the method uses the parsed information to get a list
    contains QuoteModel objects and return the list.
    """

    supported_file_type = ['pdf']

    @classmethod
    def parse(cls, filename: str) -> List[QuoteModel]:
        """Read a given pdf file, build a list that \
        contains QuoteModel objects.

        :param filename: path of file and file name, it shall be a string.
        :return: a list contains QuoteModel objects.
        """
        if not cls.can_ingest(filename):
            raise ValueError

        temp_txt_file = 'temp.txt'
        sh = subprocess.call(['pdftotext', filename, temp_txt_file])
        parse_list = list()

        with open(temp_txt_file, 'r') as f:
            lines = f.readlines()

            for line in lines:
                line = line.strip('\r\n')
                if len(line) >= 2:
                    quote_model_info = [x.strip() for x in line.split('-')]
                    body = quote_model_info[0].strip('"')
                    author = quote_model_info[1].strip()
                    qm = QuoteModel(body, author)
                    parse_list.append(qm)
        os.remove(temp_txt_file)
        return parse_list
