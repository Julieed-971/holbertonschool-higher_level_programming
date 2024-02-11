#!/usr/bin/python3
"""Script that contain a class defining a rectangle"""


class Rectangle:
    """This is an empty class that defines a rectangle."""
    pass

    def __init__(self, width=0, height=0):
        """Initialize the rectangle width and height

        Parameters
        ----------
        width : int, optional
            Width of the rectangle, optional
        Default=0
        height : int, optional
            Height of the rectangle, optional
        Default=0
         """

        self.height = height
        self.width = width

    @property
    def width(self):
        '''Get the width of a rectangle

          Returns:
        width
            width of a rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of a rectangle as private attribute

        Parameters
        ----------
        value : int
            Width of the rectangle

        Raises
        ------
        TypeError
            If the value provided is not of integer type
        ValueError
            If the value is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Get the height of a rectangle

          Returns:
        height
            height of a rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of a rectangle as private attribute

        Parameters
        ----------
        value : int
            Height of the rectangle

        Raises
        ------
        TypeError
            If the value provided is not of integer type
        ValueError
            If the value is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
