#!/usr/bin/python3
"""
A module to test a max integer function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A class for various testcases for max integer function
    """

    def test_empty_list(self):
        """
        tests an empty list
        """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_list(self):
        """
        tests a list of numbers
        """
        new_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(new_list), 4)

    def test_max_first(self):
        """
        tests when max is the first element
        """
        new_list = [4, 1, 2, 3]
        self.assertEqual(max_integer(new_list), 4)

    def test_one_element(self):
        """
        test one element in list
        """
        new_list = [2]
        self.assertEqual(max_integer(new_list), 2)

    def test_floats(self):
        """
        tests floats in a list
        """
        new_list = [2.2, 3.1, 7.8, 5.6]
        self.assertEqual(max_integer(new_list), 7.8)

    def test_ints_floats(self):
        """
        tests both ints and floats in list
        """
        new_list = [2, 3, 4.5, 8, 10.2]
        self.assertEqual(max_integer(new_list), 10.2)

    def test_string(self):
        """
        test a string
        """
        new_string = "stephen"
        self.assertEqual(max_integer(new_string), 't')

    def test_strings_list(self):
        """
        tests strings in a list
        """
        new_list = ["stephen", "james", "andrew", "arnold"]
        self.assertEqual(max_integer(new_list), "stephen")

    def tests_empty_string(self):
        """
        tests an empty string
        """
        new_string = ""
        self.assertEqual(max_integer(new_string), None)


if __name__ == "__main__":
    unittest.main()
