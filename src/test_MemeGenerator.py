import unittest
import os
from MemeGenerator.MemeGenerator import MemeEngine
from MemeGenerator.MemeRandom import MemeRandomMethod1


class TestMemeGenerator(unittest.TestCase):

    def setUp(self):
        self.mg_obj = MemeEngine('./')

    def test_init(self):
        self.assertEqual(self.mg_obj.font_path, os.path.abspath('.') + '/_data/Fonts/')
        self.assertEqual(self.mg_obj.image_extension, '')
        self.assertEqual(self.mg_obj.meme_interface, MemeRandomMethod1)
        self.assertEqual(self.mg_obj.supported_image_type, ['png', 'jpg', 'jpeg'])
        self.assertEqual(self.mg_obj.output_dir, './')

    def test_check_image(self):
        res_1 = self.mg_obj.check_image('./_data/photos/Naruto/Gaara.jpg')
        self.assertEqual(res_1, True)
        res_2 = self.mg_obj.check_image('./_data/photos/Naruto/Gaara1.jpg')
        self.assertEqual(res_2, False)

    def test_get_random_mem_name(self):
        self.mg_obj.image_extension = 'jpg'
        res = self.mg_obj.get_random_mem_name('./static')
        pos = res.rfind('.')
        self.assertGreaterEqual(int(res[0:pos]), 0)
        self.assertLessEqual(int(res[0:pos]), 1000000)

    def test_make_meme(self):
        img_path = './_data/photos/Naruto/Gaara.jpg'
        text = 'For Unit Test'
        author = 'Han Di'
        output = self.mg_obj.make_meme(img_path, text, author)
        self.assertEqual(os.path.exists(output), True)
        os.remove(output)

    def tearDown(self):
        print("Unit Test of MemeGenerator is done.")


if __name__ == "__main__":
    unittest.main()
