import unittest
from QuoteEngine.CSVIngestor import CSVIngestor


class TestCSVIngestor(unittest.TestCase):

    def setUp(self):
        self.ci_class = CSVIngestor

    def test_parse(self):
        qm = self.ci_class.parse('./_data/NarutoQuotes/NarutoQuotesCSV.csv')
        self.assertEqual(qm[0].body, 'The fire will illuminate the village')
        self.assertEqual(qm[0].author, 'Minato')
        self.assertEqual(qm[1].body, 'Destroy the enemy')
        self.assertEqual(qm[1].author, 'Gaara')
        self.assertEqual(qm[2].body, 'Do not focus on small thing')
        self.assertEqual(qm[2].author, 'Itachi')

        try:
            self.ci_class.parse('./_data/NarutoQuotes/NarutoQuotesPDF.pdf')
        except ValueError:
            self.assertRaises(ValueError)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
