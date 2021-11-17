import unittest
from QuoteEngine.DocxIngestor import DocxIngestor


class TestDocxIngestor(unittest.TestCase):

    def setUp(self):
        self.ci_class = DocxIngestor

    def test_parse(self):
        qm = self.ci_class.parse('./_data/NarutoQuotes/NarutoQuotesDOCX.docx')
        self.assertEqual(qm[0].body, 'I decide to keep going forward')
        self.assertEqual(qm[0].author, 'Naruto')
        self.assertEqual(qm[1].body, 'Wherever leaf fly, there is a fire burning')
        self.assertEqual(qm[1].author, 'Hiruzen')
        self.assertEqual(qm[2].body, 'Only memories will never die')
        self.assertEqual(qm[2].author, 'Tsunade')

        try:
            self.ci_class.parse('./_data/NarutoQuotes/NarutoQuotesTXT.txt')
        except ValueError:
            self.assertRaises(ValueError)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
