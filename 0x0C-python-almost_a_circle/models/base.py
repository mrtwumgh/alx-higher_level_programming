#!/usr/bin/python3
"""
A module for the class Base
"""
import json


class Base:
    """
    A class to serve as the Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization method
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        returns the json string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
