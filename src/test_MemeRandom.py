import unittest
from MemeGenerator.MemeRandom import MemeRandomMethod1
from MemeGenerator.MemeExceptionManager import FontDirectoryMissingError, FontsMissingError


class TestMemeRandom(unittest.TestCase):

    def setUp(self):
        self.mr_class = MemeRandomMethod1

    def test_get_random_location(self):
        image_size = (500, 500)
        body = 'Unit Test'
        author = 'Han Di'
        font_max_height_size = 40
        font_max_size = 80
        pos = self.mr_class.get_random_location(image_size, body, author, font_max_height_size, font_max_size)
        self.assertGreaterEqual(pos[0], 0)
        self.assertLessEqual(pos[0], 500)
        self.assertGreaterEqual(pos[1], 0)
        self.assertLessEqual(pos[1], 500)

    def test_get_random_color(self):
        color_info = self.mr_class.get_random_color()
        color_r = color_info[0]
        color_g = color_info[1]
        color_b = color_info[2]
        self.assertGreaterEqual(color_r, 0)
        self.assertLessEqual(color_r, self.mr_class.rgb_max_value)
        self.assertGreaterEqual(color_g, 0)
        self.assertLessEqual(color_g, self.mr_class.rgb_max_value)
        self.assertGreaterEqual(color_b, 0)
        self.assertLessEqual(color_b, self.mr_class.rgb_max_value)

    def test_get_random_font(self):
        try:
            self.mr_class.get_random_font('./_data/test')
        except FontDirectoryMissingError:
            self.assertRaises(FontDirectoryMissingError)

        try:
            self.mr_class.get_random_font('./_data')
        except FontDirectoryMissingError:
            self.assertRaises(FontDirectoryMissingError)

        try:
            self.mr_class.get_random_font('./static')
        except FontsMissingError:
            self.assertRaises(FontsMissingError)

        font = self.mr_class.get_random_font('./_data/Fonts')
        self.assertEqual(font.split('.')[-1], 'ttf')

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
