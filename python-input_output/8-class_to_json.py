#!/usr/bin/python3
"""Return the dictionnary description of an object."""


def class_to_json(obj):
    """Return the dictionnary description of an object."""
    attributes = vars(obj)
    return attributes
