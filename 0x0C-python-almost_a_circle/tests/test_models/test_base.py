#!/usr/bin/python3
"""
Tests for the class base
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    test methods
    """
    def test_id(self):
        """
        test attribute id
        """
        base_1 = Base()
        base_2 = Base()
        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 2)

    def test_set_id(self):
        """
        tests setting id
        """
        base_5 = Base(12)
        self.assertEqual(base_5.id, 12)

    def test_nb_objects(self):
        """
        test class attribute nb_objects
        """
        Base._Base__nb_objects = 0
        base_3 = Base()
        base_4 = Base()
        self.assertEqual(base_3.id, 1)
        self.assertEqual(base_4.id, 2)

if __name__ == "__main__":
    unittest.main()
