#!/usr/bin/python3
"""
writes an object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an object to a text file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        obj_json = json.dumps(my_obj)
        f.write(obj_json)
