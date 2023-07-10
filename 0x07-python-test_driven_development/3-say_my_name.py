#!/usr/bin/python3
"""
A module that prints a name
"""


def say_my_name(first_name, last_name=""):
    """
    prints out "my name is <first name> <last name>

    Args:
        first_name: first name
        last_name: last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
