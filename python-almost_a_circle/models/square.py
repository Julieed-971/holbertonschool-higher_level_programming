#!/usr/bin/python3
"""Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square that inherits of Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialiaze a square size."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the square description."""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

    @property
    def size(self):
        """Get the size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the square size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
