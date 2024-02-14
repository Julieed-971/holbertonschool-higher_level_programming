#!/usr/bin/python3
"""Append a string at the end of a text file."""


def append_write(filename="", text=""):
    """Append a string at the end of a text file."""
    with open(filename, "a") as f:
        return f.write(text)
