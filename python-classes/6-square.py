#!/usr/bin/python3
"""Sixth task - defines an empty square"""


class Square:
    """This is an empty class that defines a square."""
    pass

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square size and position

        Parameters
        ----------
        size : int, optional
            Size of the square, optional
        Default=0

        position : tuple, optional
            Position of the square
        Default=0, 0
        """
        self.position = position
        self.size = size

    @property
    def size(self):
        """Get the size of a square

        Returns:
        size
            size of a square
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """Set the size of a square

        Parameters
        ----------
        value : int
            Size of the square

        Raises
        ------
        TypeError
            If the size is not of integer type
        ValueError
            If size is strictly inferior to zero

        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    @property
    def position(self):
        """Get the position of a square

        Returns:
        position
            position of a square
          """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of a square

          Parameters
        ----------
        value : tuple
            Position of the square

        Raises
        ------
        TypeError
            If the position is not a tuple of two integers
        """

        if not type(value) is tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of a square

        Returns:
        area
            Square of size
        """
        return self.__size**2

    def my_print(self):
        """Prints a square pattern with '#'"""

        if self.__position[1] > 0:
            print()
            for _ in range(self.__size):
                print(" "*self.__position[0]+"#"*self.__size, end="")
                print()
        elif self.__position[1] <= 0:
            for _ in range(self.__size):
                print(" "*self.__position[0]+"#"*self.__size, end="")
                print()
        if self.__size == 0:
            print()
