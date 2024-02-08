#!/usr/bin/python3
'''Trying to figure out unittest'''


def add_integer(a, b=98):
    '''Add two integer
    Sum of the two integers
    '''

    sum = 0
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    sum = a + b
    return int(sum)
