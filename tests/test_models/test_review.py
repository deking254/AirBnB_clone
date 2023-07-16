#!/usr/bin/python3

"""Test module for review"""
import unittest
from time import sleep
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """tests for review"""
    def test_no_arg(self):
        """test no argument"""
        r = Review()
        self.assertEqual(r.text, "")

    def test_unique_id(self):
        """test unique id"""
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    def test_created_at(self):
        """test creation"""
        r1 = Review()
        sleep(0.05)
        r2 = Review()
        self.assertLess(r1.created_at, r2.created_at)

    def test_update_at(self):
        """test updated_at"""
        r1 = Review()
        sleep(0.05)
        r2 = Review()
        self.assertLess(r1.updated_at, r2.updated_at)

    def test_save(self):
        """test save in review"""
        r = Review()
        sleep(0.05)
        first_save = r.updated_at
        r.save()
        self.assertLess(first_save, r.updated_at)

    def test_str(self):
        """test str in review"""
        r = Review()
        r.id = "12345"
        self.assertIn("[Review] (12345)", r.__str__())
        self.assertIn("'id': '12345'", r.__str__())

    def test_to_dict(self):
        """test dictionary for calss Review"""
        r = Review()
        self.assertIn("id", r.to_dict())
        self.assertIn("created_at", r.to_dict())
        self.assertIn("updated_at", r.to_dict())
        self.assertIn("__class__", r.to_dict())


if __name__ == "__main__":
    unittest.main()
