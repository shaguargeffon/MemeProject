import unittest
from QuoteEngine.PDFIngestor import PDFIngestor


class TestPDFIngestor(unittest.TestCase):

    def setUp(self):
        self.ci_class = PDFIngestor

    def test_parse(self):
        qm = self.ci_class.parse('./_data/NarutoQuotes/NarutoQuotesPDF.pdf')
        self.assertEqual(qm[0].body, 'We have different concepts about peace')
        self.assertEqual(qm[0].author, 'Pain')
        self.assertEqual(qm[1].body, 'Do not apologize for your efforts')
        self.assertEqual(qm[1].author, 'Naruto')

        try:
            self.ci_class.parse('./_data/NarutoQuotes/NarutoQuotesTXT.txt')
        except ValueError:
            self.assertRaises(ValueError)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
