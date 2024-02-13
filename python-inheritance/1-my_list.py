#!/usr/bin/python3
"""Create a MyList Class."""


class MyList(list):
    """MyList class that inherits of list."""
    def print_sorted(self):
        """Sorts a list."""
        print(sorted(self))
