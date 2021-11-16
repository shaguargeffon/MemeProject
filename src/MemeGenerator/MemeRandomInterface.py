"""A python module declares abstract interfaces."""

from abc import ABC, abstractmethod


class MemeRandomInterface(ABC):
    """An abstract class for getting random parameters."""

    rgb_max_value = 0
    font_type = ''

    @classmethod
    @abstractmethod
    def get_random_location(cls, image_size: tuple,
                            body: str,
                            author: str,
                            font_max_height_size: int,
                            font_max_size: int) -> tuple:
        """Abstract method."""
        pass

    @classmethod
    @abstractmethod
    def get_random_color(cls):
        """Abstract method."""
        pass

    @classmethod
    @abstractmethod
    def get_random_font(cls, font_path: str):
        """Abstract method."""
        pass
