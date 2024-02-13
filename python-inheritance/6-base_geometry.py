#!/usr/bin/python3
"""Write an empty geometry class"""


class BaseGeometry:
    """Empty geometry class"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")
