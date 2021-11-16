"""A python module defines a class TextIngestor."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """A TextIngestor object which can parse txt file.

    The class TextIngestor is inherited from IngestorInterface.
    It supplies a class method parse to parse txt file.
    Then the method uses the parsed information to get a list
    contains QuoteModel objects and return the list.
    """

    supported_file_type = ['txt']

    @classmethod
    def parse(cls, filename: str) -> List[QuoteModel]:
        """Read a given txt file, build a list that \
        contains QuoteModel objects.

        :param filename: path of file and file name, it shall be a string.
        :return: a list contains QuoteModel objects.
        """
        if not cls.can_ingest(filename):
            raise Exception('cannot ingest txt file.')

        parse_list = list()

        with open(filename, 'r') as f:
            lines = f.readlines()

            for line in lines:
                line = line.strip('\r\n')
                if len(line) >= 2:
                    quote_model_info = [x.strip() for x in line.split('-')]
                    body = quote_model_info[0].strip('"')
                    author = quote_model_info[1].strip()
                    qm = QuoteModel(body, author)
                    parse_list.append(qm)

        return parse_list
