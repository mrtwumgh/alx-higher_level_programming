#!/usr/bin/python3
"""
A module that creates a class
and inherits from list
"""


class MyList(list):
    """
    A class MyList that inherits from
    base class list
    """

    def print_sorted(self):
        """
        prints the list, sorted
        """
        print(sorted(self))
