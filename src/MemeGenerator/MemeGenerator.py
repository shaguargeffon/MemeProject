"""A python module defines a class MemeEngine."""

from PIL import Image, ImageDraw, ImageFont
import random
import os
from .MemeRandom import MemeRandomMethod1


class MemeEngine(object):
    """A Meme Engine object which can generate a meme.

    The MemeEngine class supplies three methods, check_image,
    get_random_mem_name, and make_meme.
    The method check_image checks the given image if it is valid.
    The method get_random_mem_name gets a meme name using random library.
    The method make_meme takes a image path+name, text, author and width and
    generate a meme, return the path of the generated meme.
    """

    def __init__(self, output_dir, supported_image_type=['png', 'jpg', 'jpeg'],
                 font_path='/_data/Fonts/', meme_interface=MemeRandomMethod1):
        """Instantiate the class using given parameters.

        :param output_dir: path of the output image and also output image name.
        :param supported_image_type: lists which type of images are supported.
        :param font_path: path of fonts
        :param meme_interface: strategy to get random location, color and font.
        :return: output_dir
        """
        self.output_dir = output_dir
        self.supported_image_type = supported_image_type
        self.image_extension = ''
        # font_path has to be an absolute path
        self.font_path = os.path.abspath('.') + font_path
        self.meme_interface = meme_interface
        if os.path.exists(self.output_dir):
            pass
        else:
            os.mkdir(self.output_dir)
        self.image_dir = None

    def check_image(self, image_path):
        """Check the given image if it is valid.

        :param image_path: path of image and image's name,
                            it shall be a string.
        :return: a bool value to show the check result.
        """
        try:
            im = Image.open(image_path)
            im.close()
        except FileNotFoundError:
            print("The image can't be found.")
            return False

        self.image_extension = image_path.split('.')[-1]
        if self.image_extension not in self.supported_image_type:
            print('ImageTypeException: The image type is not supported.')
            return False

        return True

    def get_random_mem_name(self, output_path) -> str:
        """Get a random meme name.

        :param output_path: path of file and file name, it shall be a string.
        :return: random image name.
        """
        image_names = os.listdir(output_path)
        while True:
            image_name = str(random.randint(0, 1000000)) + \
                         '.' + self.image_extension
            if image_name in image_names:
                continue
            else:
                return image_name

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Read a given csv file, build and return a QuoteModel object.

        :param img_path: input image, it shall be a string.
        :param text: body string
        :param author: author string
        :param width: width of the output image, optional
        :return: a QuoteModel object.
        """
        if width < 10:
            print("The requested width of image is smaller than 10, fixed to 10.")
            width = 10
        elif width > 1024:
            print("The requested width of image is larger than 1024, fixed to 1024.")
            width = 1024
        else:
            pass

        check_result = self.check_image(img_path)
        if not check_result:
            print("The given parameters can not .")
            return self.output_dir

        with Image.open(img_path).convert("RGBA") as image:
            image_width, image_height = image.size
            image_size = (width, int(image_height*width/image_width))
            im = image.resize(image_size)
            new_image = Image.new(im.mode, im.size)

            # get a random font name from font folder
            font_name = self.meme_interface.get_random_font(self.font_path)
            font = ImageFont.truetype(self.font_path + font_name,
                                      int(image_size[0]/20))
            font_size_text_width_pixel = font.getsize(text)[0]
            font_size_author_width_pixel = font.getsize(author)[0]
            font_max_width_size = max(font_size_text_width_pixel,
                                      font_size_author_width_pixel)
            font_max_height_size = max(font.getsize(text)[1],
                                       font.getsize(author)[1])
            # get a random location for body and author string
            random_mem_pos = self.meme_interface.\
                get_random_location(new_image.size, text,
                                    author,
                                    font_max_height_size,
                                    font_max_width_size)
            # draw a new image based on the given image
            d = ImageDraw.Draw(new_image)
            random_color = self.meme_interface.get_random_color()
            # add text and author to the image
            d.text((random_mem_pos[0], random_mem_pos[1]),
                   text, font=font, fill=random_color)
            author_underline = '- ' + author
            d.text((random_mem_pos[0], random_mem_pos[1]+font_max_height_size),
                   author_underline, font=font, fill=random_color)
            out = Image.alpha_composite(im, new_image)
            output = out.convert('RGB')
            mem_name = self.get_random_mem_name(self.output_dir)
            if self.output_dir[-1] == '/':
                self.image_dir = self.output_dir + mem_name
            else:
                self.image_dir = self.output_dir + '/' + mem_name
            output.save(self.image_dir)

        return self.image_dir
