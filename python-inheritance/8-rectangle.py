#!/usr/bin/python3
"""Imports a geometry class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits of BaseGeometry class."""

    def __init__(self, width, height):
        """Initialize width and height of a rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("heigth", height)
        self.__width = width
        self.__height = height
