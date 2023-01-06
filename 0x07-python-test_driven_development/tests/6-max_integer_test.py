#!/usr/bin/python3
"""
Unittests for the module 6-max_integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the function max_integer"""
    
    def test_max_integer(self):
        """Test a list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1]), 1)

    def test_large_integers(self):
        """Test a list of large integers"""
        self.assertEqual(max_integer([100_000_000, 200_000_000, 300_000_000]), 300_000_000)

    def test_negative_integers(self):
        """Test a list of negative integers"""
        self.assertEqual(max_integer([-100_000_000, -200_000_000, -300_000_000]), -100_000_000)

    def test_small_larger_integers(self):
        """Test a list of positive and negative integers"""
        self.assertEqual(max_integer([100, -100, 200, -200]), 200)

    def test_floating_numbers(self):
        """Test a list of floating point numbers"""
        self.assertRaises(TypeError, max_integer, [1.5, 2.5, 3.5]

    def test_empty_list(self):
        """Tests an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_non_integer(self):
        """Test non-integer types"""
        self.assertRaises(TypeError, max_integer, ['a', 'b', 'c'])

    def test_mix_types(self):
        """Tests a mix of integer and non-integer types"""
        self.assertRaises(TypeError, max_integer, [1, 'b', 2])
        self.assertRaises(TypeError, max_integer, [1, 'b', 2, 3])

if __name__ == '__main__':
    unittest.main()
