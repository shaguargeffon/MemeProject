import unittest
from QuoteEngine.IngestorInterface import IngestorInterface


class TestIngestorInterface(unittest.TestCase):

    def setUp(self):
        self.ii_class = IngestorInterface

    def test_can_ingest(self):
        self.ii_class.supported_file_type = ['csv', 'pdf', 'docx', 'txt']
        res = self.ii_class.can_ingest('./_data/NarutoQuotes/NarutoQuotesCSV.csv')
        self.assertEqual(res, True)

        res = self.ii_class.can_ingest('./_data/NarutoQuotes/NarutoQuotesCSV.c')
        self.assertEqual(res, False)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
