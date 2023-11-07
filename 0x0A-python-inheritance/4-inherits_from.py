#!/usr/bin/python3
"""
A module that returns True if object
is a subclass of an object
"""


def inherits_from(obj, a_class):
    """
    A function that returns True if
    object is a subclass of an object
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
