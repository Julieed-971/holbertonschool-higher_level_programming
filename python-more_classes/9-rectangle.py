#!/usr/bin/python3
"""Script that contain a class defining a rectangle"""


class Rectangle:
    """This is an empty class that defines a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = self.print_symbol

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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of a rectangle

        Returns:
        area
            Area of a rectangle
        """

        return self.__width*self.__height

    def perimeter(self):
        """Calculate the perimeter of a rectangle

        Returns:
        perimeter
            Perimeter of a rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2*(self.__height+self.__width)

    def __str__(self):
        """Prints a rectangle pattern with '#'"""
        rectangle_str = ""
        if self.__height == 0 or self.__width == 0:
            return rectangle_str
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str += str(self.print_symbol)
            if i != self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
