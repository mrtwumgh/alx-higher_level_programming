#!/usr/bin/python3
"""
Reads from a textfile
"""


def read_file(filename=""):
    """
    A function that reads from a file
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
