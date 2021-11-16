"""A python module builds a method to get random parameter for meme."""

import os
import random
from .MemeRandomInterface import MemeRandomInterface
from .MemeExceptionManager import FontsMissingError, FontDirectoryMissingError


class MemeRandomMethod1(MemeRandomInterface):
    """A set of methods to get random parameters for a meme.

    The class MemeRandomMethod1 is inherited from MemeRandomInterface.
    """

    rgb_max_value = 255
    font_type = 'ttf'

    @classmethod
    def get_random_location(cls, image_size: tuple,
                            body: str, author: str,
                            font_max_height_size: int,
                            font_max_size: int) -> tuple:
        """Get a random location.

        :param image_size: size of image, it is a tuple (width, height)
        :param body: body string
        :param author: author string
        :param font_max_height_size: maximal height of body and author
        :param font_max_size: maximal width of body and author
        :return: a tuple contains width and height of the random position
        """
        if image_size[0] < font_max_size:
            position_width = 0
        else:
            temp_size = image_size[0] - font_max_size
            position_width = random.randint(0, temp_size)

        if image_size[1] < font_max_height_size*2:
            position_height = 0
        else:
            temp_size = image_size[1] - font_max_height_size*2
            position_height = random.randint(0, temp_size)
        return position_width, position_height

    @classmethod
    def get_random_color(cls) -> tuple:
        """Get random color."""
        color_r = random.randint(0, cls.rgb_max_value)
        color_g = random.randint(0, cls.rgb_max_value)
        color_b = random.randint(0, cls.rgb_max_value)
        return color_r, color_g, color_b, cls.rgb_max_value

    @classmethod
    def get_random_font(cls, font_path: str) -> str:
        """Get a random font.

        :param font_path: path of font and font name, it shall be a string.
        :return: a font with string format
        """
        if os.path.exists(font_path):
            pass
        else:
            raise FontDirectoryMissingError

        fonts = os.listdir(font_path)
        if fonts:
            while True:
                font = random.choice(fonts)
                if font.split('.')[-1] == cls.font_type:
                    return font
        else:
            raise FontsMissingError
