"""A python module defines a class QuoteModel."""


class QuoteModel(object):
    """A QuoteModel object which holds two attributes: body and author."""

    def __init__(self, body, author):
        """Initialize a QuoteModel object.

        :param body: text information which shall be a string.
        :param author: text information which shall be a string.
        :return: None
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Use the two attributes body and author to build a machine-readable \
        information about the object.

        :param : None
        :return: Machine-readable information about the object.
        """
        return f'{self.body} - {self.author}'

    def __str__(self):
        """Use the two attributes body and author to build a user-readable \
        information about the object.

        :param : None
        :return: user-readable information about the object.
        """
        return f'"{self.body}" - {self.author}'
