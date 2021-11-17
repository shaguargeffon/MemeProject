"""A python module defines a class CSVIngestor."""

from typing import List
import pandas
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """A CSVIngestor object which can parse csv file.

    The class CSVIngestor is inherited from IngestorInterface.
    It supplies a class method parse to parse csv file.
    Then the method uses the parsed information to get a list
    contains QuoteModel objects and return the list.
    """

    supported_file_type = ['csv']

    @classmethod
    def parse(cls, filename: str) -> List[QuoteModel]:
        """Read a given csv file, build a list that \
        contains QuoteModel objects.

        :param filename: path of file and file name, it shall be a string.
        :return: a list contains QuoteModel objects.
        """
        if not cls.can_ingest(filename):
            raise ValueError

        parse_list = list()
        csv_handle = pandas.read_csv(filename, header=0)

        for index, row in csv_handle.iterrows():
            qm = QuoteModel(row['body'], row['author'])
            parse_list.append(qm)
        return parse_list
