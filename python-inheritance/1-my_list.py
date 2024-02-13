#!/usr/bin/python3
"""MyList Class."""


class MyList(list):
    """MyList class that inherits 'from' list."""
    
    def print_sorted(self):
        """Sorts a list."""
        print(sorted(self))
