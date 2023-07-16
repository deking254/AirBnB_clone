#!/usr/bin/python3

"""Test module for class Amenity"""
import unittest
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """tests for Amenity"""
    def test_no_arg(self):
        """no argument"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_unique_id(self):
        """test unique id"""
        am = Amenity()
        am1 = Amenity()
        self.assertNotEqual(am.id, am1.id)

    def test_created_at(self):
        """test creation"""
        am = Amenity()
        sleep(0.05)
        am1 = Amenity()
        self.assertLess(am.created_at, am1.created_at)

    def test_updated_at(self):
        """test updated at"""
        am = Amenity()
        sleep(0.05)
        am1 = Amenity()
        self.assertLess(am.updated_at, am1.updated_at)

    def test_str(self):
        """test str method"""
        am = Amenity()
        am.id = "12345"
        self.assertIn("[Amenity] (12345)", am.__str__())
        self.assertIn("'id': '12345'", am.__str__())

    def test_save(self):
        """test save in Amenity"""
        am = Amenity()
        sleep(0.05)
        first_save = am.updated_at
        am.save()
        self.assertLess(first_save, am.updated_at)

    def test_to_dict(self):
        """test dictionary in amenity"""
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())


if __name__ == "__main__":
    unittest.main()
