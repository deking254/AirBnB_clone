#!/usr/bin/python3

"""test module for class city"""
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for class City"""
    def test_unique_id(self):
        """test for unique id"""
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)

    def test_created_at(self):
        """test creation"""
        c1 = City()
        sleep(0.05)
        c2 = City()
        self.assertLess(c1.created_at, c2.created_at)

    def test_updated_at(self):
        """test update_at"""
        c1 = City()
        sleep(0.05)
        c2 = City()
        self.assertLess(c1.updated_at, c2.updated_at)

    def test_name_type(self):
        """test type of name"""
        self.assertEqual(str, type(City.name))

    def test_save(self):
        """test save for city """
        c1 = City()
        sleep(0.05)
        first_save = c1.updated_at
        c1.save()
        self.assertLess(first_save, c1.updated_at)

    def test_no_attributr(self):
        """test class without attr"""
        c1 = City()
        self.assertEqual(c1.name, "")

    def test_to_dict(self):
        """test dictionary in city class"""
        c1 = City()
        self.assertIn("id", c1.to_dict())
        self.assertIn("created_at", c1.to_dict())
        self.assertIn("updated_at", c1.to_dict())
        self.assertIn("__class__", c1.to_dict())

    def test_str(self):
        """test str in city"""
        c = City()
        c.id = "12345"
        self.assertIn("[City] (12345)", c.__str__())
        self.assertIn("'id': '12345'", c.__str__())


if __name__ == "__main__":
    unittest.main()
