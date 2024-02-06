#!/usr/bin/python3
"""Fifth task - defines an empty square"""


class Square:
    """This is an empty class that defines a square."""
    pass

    def __init__(self, size=0):
        """Initialize the size

        Parameters
        ----------
        size : int, optional
            Size of the square, optional
        Default=0
        """

        self.__size = size

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

    def area(self):
        """Calculate the area of a square

        Returns:
        area
            Square of size
        """
        return self.__size**2

    def my_print(self):
        """Prints a square pattern with '#'"""

        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        print()
