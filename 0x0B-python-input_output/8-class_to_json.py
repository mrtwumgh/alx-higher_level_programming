#!/usr/bin/python3
""""
returns the dictionary description with a simple
data structure(list, dictionary, string, integer
boolean)
"""


def class_to_json(obj):
    """
    a function that returns a dictionary description
    with a simple data structure(list, dictionary, string,
    integer, boolean)
    """
    result = {}
    for key, value in obj.__dict__.items():
        if type(value) in [list, dict, str, int, bool]:
            result[key] = value
    return result
