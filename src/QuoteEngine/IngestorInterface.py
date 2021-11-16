"""Parse different kinds of files according to the given classes.

The IngestorInterface is an abstract class. It supplies an interface
parse for its children.
"""

from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """An ingestor to check format of given filename and parse it."""

    supported_file_type = []

    @classmethod
    def can_ingest(cls, filename) -> bool:
        """Check if the extension of given filename is in the defined list.

        :param filename: path of file and file name, it shall be a string.
        :return: True-> the extension of given filename is in the defined list
            False-> the extension of given filename is not in the defined list
        """
        extension = filename.split('.')[-1]
        if extension in cls.supported_file_type:
            return True
        else:
            return False

    @classmethod
    @abstractmethod
    def parse(cls, filename: str):
        """Unimplemented interface for children classes."""
        pass
