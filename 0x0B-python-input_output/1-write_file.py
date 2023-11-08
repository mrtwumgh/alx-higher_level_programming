#!/usr/bin/python3
"""
A module that writes to a file
"""


def write_file(filename="", text=""):
    """
    A function that writes to a file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
