#!/usr/bin/python3
"""Write an empty geometry class."""


class BaseGeometry:
    """Empty geometry class."""

    def area(self):
        """Raise an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
