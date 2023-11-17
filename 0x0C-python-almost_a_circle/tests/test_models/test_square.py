#!/usr/bin/python3
"""
A test module to test the class square
"""
import unittest
from models.square import Square
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    """
    A class to test the class Square
    """

    def setUp(self):
        """
        setUp instances of square
        """
        self.s1 = Square(5, 2, 3, 1)
        self.s2 = Square(3, 1, 1)
        self.s3 = Square(4, 0, 0)
        self.s4 = Square(8, 2, 4)

    def test_attributes(self):
        """
        test initialized attributes
        """
        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s1.height, 5)
        self.assertEqual(self.s1.x, 2)
        self.assertEqual(self.s1.y, 3)

    def test_id_inheritance(self):
        """
        test case for checking if Square inherits id
        """
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 10)

    def test_setters_values(self):
        """
        tests the validity of values for setters
        """
        self.s3.size = 7
        self.s3.x = 3
        self.s3.y = 5

        self.assertEqual(self.s3.size, 7)
        self.assertEqual(self.s3.x, 3)
        self.assertEqual(self.s3.y, 5)

    def test_invalid_values(self):
        """
        tests invalid values for setters
        """
        with self.assertRaises(TypeError):
            self.s3.width = "invalid_width"
        with self.assertRaises(ValueError):
            self.s3.width = 0
        with self.assertRaises(TypeError):
            self.s3.x = "invalid_x"
        with self.assertRaises(ValueError):
            self.s3.x = -3
        with self.assertRaises(TypeError):
            self.s3.y = "invalid_y"
        with self.assertRaises(ValueError):
            self.s3.y = -4

    def test_area(self):
        """
        tests area method
        """
        self.assertEqual(self.s3.area(), 16)
        self.assertEqual(self.s4.area(), 64)

    def test_display(self):
        """
        tests the display method
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        self.s3.display()

        sys.stdout = sys.__stdout__
        expected_output = "####\n" * 4
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        """
        test magic method str
        """
        self.assertEqual(str(self.s3), "[Square] (20) 0/0 - 4")

    def test_update_args(self):
        """
        tests update method args
        """
        self.s3.update(10, 3, 2, 1)

        self.assertEqual(self.s3.id, 10)
        self.assertEqual(self.s3.size, 3)
        self.assertEqual(self.s3.x, 2)
        self.assertEqual(self.s3.y, 1)

    def test_update_kwargs(self):
        """
        tests update method kwargs
        """
        self.s3.update(size = 5, y = 3)
        self.assertEqual(self.s3.size, 5)
        self.assertEqual(self.s3.y, 3)

    def tearDown(self):
        """
        tear down instances
        """
        del self.s1
        del self.s2
        del self.s3
        del self.s4


if __name__ == "__main__":
    unittest.main()
