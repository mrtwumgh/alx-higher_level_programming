#!/usr/bin/python3
"""
A module to test the base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import json


class TestBaseClass(unittest.TestCase):
    """
    Various tests to test Base Class
    """

    def setUp(self):
        """
        sets up the object
        """
        self.b1 = Base()
        self.b2 = Base(10)

    def test_init(self):
        """
        tests the init method
        """
        self.assertEqual(self.b1.id, 2)
        self.assertEqual(self.b2.id, 10)

    def test_class_attribute(self):
        """
        tests the class attribute
        """
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_to_json_string_empty(self):
        """
        tests an empty list
        """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        """
        tests case for none input
        """
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_valid(self):
        """
        tests a valid input
        """
        dicts = [{
            "id": 1,
            "name": "Al"
            },
            {
            "id": 2,
            "name": "Jam"
        }]
        result = Base.to_json_string(dicts)
        expected_result = '[{"id": 1, "name": "Al"}, {"id": 2, "name": "Jam"}]'
        self.assertEqual(result, expected_result)

    def test_save_to_file_empty(self):
        """
        tests an empty list
        """
        Base.save_to_file([])
        self.assertTrue(os.path.exists("Base.json"))
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_none(self):
        """
        tests case for none input
        """
        Base.save_to_file(None)
        self.assertTrue(os.path.exists("Base.json"))
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_valid(self):
        """
        test a valid input
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = json.load(file)
            self.assertEqual(content[0]['width'], 10)
            self.assertEqual(content[0]['height'], 7)
            self.assertEqual(content[0]['x'], 2)
            self.assertEqual(content[0]['y'], 8)
            self.assertEqual(content[1]['width'], 2)
            self.assertEqual(content[1]['height'], 4)
            self.assertEqual(content[1]['x'], 0)
            self.assertEqual(content[1]['y'], 0)

    def tearDown(self):
        """
        teardown of objects
        """
        del self.b1
        del self.b2
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectanggle.json"):
            os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
