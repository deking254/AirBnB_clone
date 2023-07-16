#!/usr/bin/python3

"""test module for class place"""
import unittest
from time import sleep
import models
from models.place import Place


class TestPlace(unittest.TestCase):
    """test for class place"""
    def test_no_arg(self):
        """test no argument"""
        p = Place()
        self.assertEqual(p.name, "")

    def test_str(self):
        """test str in class"""
        p = Place()
        p.id = "12345"
        self.assertIn("[Place] (12345)", p.__str__())
        self.assertIn("'id': '12345'", p.__str__())

    def test_save(self):
        """test save"""
        p = Place()
        sleep(0.05)
        first_save = p.updated_at
        p.save()
        self.assertLess(first_save, p.updated_at)

    def test_to_dict(self):
        """test dictionary in place"""
        p = Place()
        self.assertIn("id", p.to_dict())
        self.assertIn("created_at", p.to_dict())
        self.assertIn("updated_at", p.to_dict())
        self.assertIn("__class__", p.to_dict())

    def test_unique_id(self):
        """test unique id"""
        p = Place()
        sleep(0.05)
        p1 = Place()
        self.assertNotEqual(p.id, p1.id)

    def test_storage(self):
        """test storage"""
        self.assertIn(Place(), models.storage.all().values())

    def test_created_at(self):
        """test creation"""
        p = Place()
        sleep(0.05)
        p1 = Place()
        self.assertLess(p.created_at, p1.created_at)

    def test_updated_at(self):
        """test updated at"""
        p = Place()
        sleep(0.05)
        p1 = Place()
        self.assertLess(p.updated_at, p1.updated_at)


if __name__ == "__main__":
    unittest.main()
