#!/usr/bin/python3
"""
a module that returns true if
object is an instance of class
"""


def is_kind_of_class(obj, a_class):
    """
    a function that returns true if
    object is kind of class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
