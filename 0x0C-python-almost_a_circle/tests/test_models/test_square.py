#!/usr/bin/python3
"""
A module to test the class Square
"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    methods to test the class
    """
    def test_init(self):
        """
        tests initialization
        """
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

        s1 = Square(3, 1, 2, 99)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.height, 3)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 99)

    def test_str(self):
        s = Square(5)
        output = f"[Square] ({s.id}) {s.x}/{s.y} - {s.width}"
        self.assertEqual(str(s), output)
