#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""
A unittest to test the function 6-max_integer
"""


class TestMaxInteger(unittest.TestCase):
    """
    Class that defines tests for 6-max_integer
    """

    def test_positive_integers(self):
        """
        tests if list items are positive
        """
        pos_ints = [1, 2, 3, 4]
        self.assertEqual(max_integer(pos_ints), 4)

    def test_max_at_beginning(self):
        """
        tests max at beginning
        """
        max_at_beg = [4, 1, 2, 3]
        self.assertEqual(max_integer(max_at_beg), 4)

    def test_max_at_middle(self):
        """
        tests max in the middle
        """
        max_in_mid = [1, 2, 5, 3, 4]
        self.assertEqual(max_integer(max_in_mid), 5)

    def test_one_neg(self):
        """
        tests one negative number in list
        """
        one_neg = [1, 2, -3, 4, 5]
        self.assertEqual(max_integer(one_neg), 5)

    def test_negative_integers(self):
        """
        test if list items are negative
        """
        neg_ints = [-1, -3, -4, -6]
        self.assertEqual(max_integer(neg_ints), -1)

    def test_one_element(self):
        """
        test one element
        """
        one_elem = [3]
        self.assertEqual(max_integer(one_elem), 3)

    def test_floats(self):
        """
        test for float number
        """
        floats = [2.1, 2, 3.8]
        self.assertEqual(max_integer(floats), 3.8)

    def test_empty_list(self):
        """
        tests for an empty list
        """
        self.assertEqual(max_integer(), None)

    def test_non_integer(self):
        """
        tests for non-integer
        """
        with self.assertRaises(TypeError):
            max_integer([2, 3, "Five", 4])


if __name__ == "__main__":
    unittest.main()
