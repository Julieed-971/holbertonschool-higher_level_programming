#!/usr/bin/python3
"""Rectangle class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square that inherits of Rectangle class."""

    def __init__(self, size):
        """Initialiaze a square size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate the area of a square."""
        return self.__size**2
