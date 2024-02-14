#!/usr/bin/python3
"""Read a text file and prints it to stdout."""


def read_file(filename=""):
    """Read a text file and prints it to stdout."""
    with open(filename, "r") as fobj:
        text = fobj.read()
    print(text.rstrip('\n'), end="")
