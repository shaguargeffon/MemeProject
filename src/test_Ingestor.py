import unittest
from QuoteEngine.Ingestor import Ingestor


class TestIngestor(unittest.TestCase):

    def setUp(self):
        self.i_class = Ingestor

    def test_parse(self):
        res = self.i_class.parse('./_data/NarutoQuotes/NarutoQuotesCSV.csv')
        self.assertEqual(res[0].body, 'The fire will illuminate the village')
        self.assertEqual(res[0].author, 'Minato')
        self.assertEqual(res[1].body, 'Destroy the enemy')
        self.assertEqual(res[1].author, 'Gaara')
        self.assertEqual(res[2].body, 'Do not focus on small thing')
        self.assertEqual(res[2].author, 'Itachi')

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
