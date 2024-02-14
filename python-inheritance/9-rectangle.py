#!/usr/bin/python3
"""Geometry class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits of BaseGeometry class."""

    def __init__(self, width, height):
        """Initialize the width and height of a rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of a rectangle.

        Returns:
        area
            Area of a rectangle
        """
        return self.__width*self.__height

    def __str__(self):
        """Return the rectangle description."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
