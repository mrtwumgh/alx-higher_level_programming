#!/usr/bin/python3
"""
a module that creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """
    a function that creates an object from a json file
    """
    with open(filename, encoding="utf-8") as f:
        json_file = f.read()
        return json.loads(json_file)
