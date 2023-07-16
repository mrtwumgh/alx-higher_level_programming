#!/usr/bin/python3
"""
writes a string to a text filee
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
