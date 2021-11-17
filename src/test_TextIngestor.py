import unittest
from QuoteEngine.TextIngestor import TextIngestor


class TestTextIngestor(unittest.TestCase):

    def setUp(self):
        self.ci_class = TextIngestor

    def test_parse(self):
        qm = self.ci_class.parse('./_data/NarutoQuotes/NarutoQuotesTXT.txt')
        self.assertEqual(qm[0].body, 'Youth has no end')
        self.assertEqual(qm[0].author, 'Sasori')
        self.assertEqual(qm[1].body, 'I understand because I lost')
        self.assertEqual(qm[1].author, 'Kakashi')
        self.assertEqual(qm[2].body, 'I am the root buried in the dark')
        self.assertEqual(qm[2].author, 'Danzou')

        try:
            self.ci_class.parse('./_data/NarutoQuotes/NarutoQuotesPDF.pdf')
        except ValueError:
            self.assertRaises(ValueError)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
