#!/usr/bin/python3
"""
Module that returns addition of 2 integers
"""


def add_integer(a, b=98):
    """
    This function returns the addition of 2 integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
