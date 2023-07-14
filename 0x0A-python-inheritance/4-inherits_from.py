#!/usr/bin/python3
"""
A module that checks
if an object is a subclass of a
class
"""


def inherits_from(obj, a_class):
    """
    a function that checks
    if an object is a subclass of a
    class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
