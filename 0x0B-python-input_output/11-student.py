#!/usr/bin/python3
"""
A module of a class student
"""


class Student:
    """
    A class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        initializes a new instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of Student
        """
        if isinstance(attrs, list) and \
           all(isinstance(item, str) for item in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the student instance
        """
        for k, v in json.items():
            setattr(self, k, v)
