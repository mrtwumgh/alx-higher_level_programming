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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the json string representation
        """
        list_dicts = []
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the string representation to file
        """
        list_dicts = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                for objs in list_objs:
                    list_dicts.append(objs.to_dictionary())
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of json string representation
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
