#!/usr/bin/python3
'''Function that prints a square with the character #'''


def print_square(size):
    '''
    Function that prints a square with the character #

    Parameters
    ----------
    size: int
        size of the square

    Raises
    ------
    TypeError
        If size is not an integer or less than zero
    ValueError
        If size is less than zero

    Returns
    -------
    None
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for x in range(size):
        print("#" * size)
