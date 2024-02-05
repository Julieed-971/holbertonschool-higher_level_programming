#!/usr/bin/python3
"""Third task - defines an empty square"""


class Square:
    """This is an empty class that defines a square."""
    pass

    def __init__(self, size=0):
        """
        This function initialize the size
        and check if size is an integer
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
