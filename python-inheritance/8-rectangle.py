#!/usr/bin/python3
"""Imports a geometry class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits of BaseGeometry class."""

    def __init__(self, width, height):
        """Initialize width and height of a rectangle.

        Parameters
        ----------
        width : int
            Width of the rectangle
        height : int
            Height of the rectangle

        Raises
        ------
        TypeError
            If the width or the height are not integers

        """
        self.integer_validator("width", width)
        self.integer_validator("heigth", height)
        self.__width = width
        self.__height = height
