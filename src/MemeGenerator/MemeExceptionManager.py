"""A python module defines exceptions."""


class FontsMissingError(FileNotFoundError):
    """self-defined exception FontsMissingError."""

    pass


class FontDirectoryMissingError(FileNotFoundError):
    """self-defined exception FontDirectoryMissingError."""

    pass
