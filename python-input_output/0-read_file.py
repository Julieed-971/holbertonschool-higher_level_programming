#!/usr/bin/python3
"""Reads a text file and prints it to stdout"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, "r") as fobj:
        text = fobj.read()
    print(text, end="")
