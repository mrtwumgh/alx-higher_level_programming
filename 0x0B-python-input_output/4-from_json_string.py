#!/usr/bin/python3
"""
A module that returns an object represented
by a JSON string
"""
import json


def from_json_string(my_string):
    """
    A function that returns an object represent
    by a JSON string
    """
    return json.loads(my_string)
