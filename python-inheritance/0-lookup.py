#!/usr/bin/python3
"""Looks up for a list of attributes and methods of an object"""


def lookup(obj):
    """Looks up for a list of attributes and methods of an object"""
    return list(dir(obj))
