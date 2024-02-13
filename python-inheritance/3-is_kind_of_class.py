#!/usr/bin/python3
"""Checks if the object is an instance of,
or if the object is an instance of a class
that inherited of, the specified class"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of,
or if the object is an instance of a class
that inherited of, the specified class"""
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
