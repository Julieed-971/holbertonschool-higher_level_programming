#!/usr/bin/python3
"""Returns Trus if object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Returns True if object is exactly an instance of the specified class"""
    if type(obj) is a_class and a_class != object:
        return True
    if type(obj) is object:
        return False
    return False
