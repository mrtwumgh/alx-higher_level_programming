#!/usr/bin/python3.11
"""
A add_integer module
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b

    Args:
        a: first integer
        b: second integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
