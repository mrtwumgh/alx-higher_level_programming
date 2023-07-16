#!/usr/bin/python3
"""
a module that returns an object(python data structure)
"""
import json


def from_json_string(my_str):
    """
    a function that returns an object
    """
    return json.loads(my_str)
