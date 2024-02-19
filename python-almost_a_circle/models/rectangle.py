#!/usr/bin/python3
"""Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle width, height, x, y and id"""

        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of a rectangle"""
        self.__width = value

    @property
    def height(self):
        """Get the height of a rectangle"""
        return self.__height

    @width.setter
    def height(self, value):
        """Set the height of a rectangle"""
        self.__height = value

    @property
    def x(self):
        """Get the horizontal position of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the horizontal position of the rectangle"""
        self.__x = value

    @property
    def y(self):
        """Get the vertical position of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical position of the rectangle"""
        self.__y = value
