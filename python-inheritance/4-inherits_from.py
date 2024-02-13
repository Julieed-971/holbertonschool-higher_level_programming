#!/usr/bin/python3
"""Checks if the object is an instance of a class that inherited
(directly or indirectly) of the specified class"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited
(directly or indirectly) of the specified class"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
