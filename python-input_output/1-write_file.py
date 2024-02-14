#!/usr/bin/python3
"""Write a string to a text file (UTF8) and
returns the number of characters written."""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, "w") as f:
        return f.write(text)
