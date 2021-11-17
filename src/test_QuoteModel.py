import unittest
from QuoteEngine.QuoteModel import QuoteModel


class TestQuoteModel(unittest.TestCase):

    def setUp(self):
        self.qm_obj = QuoteModel('aaa', 'bbb')

    def test_init(self):
        self.assertEqual(self.qm_obj.body, 'aaa')
        self.assertEqual(self.qm_obj.author, 'bbb')

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
