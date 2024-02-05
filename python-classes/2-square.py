#!/usr/bin/python3
"""Third task - defines an empty square"""


class Square:
    """This is an empty class that defines a square."""

    def __init__(self, size=0):
        """Initialize the size and check if size is an integer

        Parameters
        ----------
        size : int, optional
            Size of the square, optional
        Default=0

        Raises
        ------
        TypeError
            If the size is not of integer type
        ValueError
            If size is strictly inferior to zero

        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
