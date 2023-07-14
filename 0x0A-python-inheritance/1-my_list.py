#!/usr/bin/python3
"""
A module that inherits from list
"""


class MyList(list):
    """
    MyList inherits from list
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
