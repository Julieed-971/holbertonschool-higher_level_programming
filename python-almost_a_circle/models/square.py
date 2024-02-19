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
