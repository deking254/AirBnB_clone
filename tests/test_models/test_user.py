#!/usr/bin/python3

"""Test module for class User"""
import unittest
from time import sleep
from models.user import User


class TestUser(unittest.TestCase):
    """tests for User class"""
    def test_no_arg(self):
        """ no arg"""
        self.assertEqual(User, type(User()))

    def test_created_at(self):
        """test creation"""
        u = User()
        sleep(0.05)
        u1 = User()
        self.assertLess(u.created_at, u1.created_at)

    def test_updated_at(self):
        """test updated"""
        u = User()
        sleep(0.05)
        u1 = User()
        self.assertLess(u.created_at, u1.created_at)

    def test_str(self):
        """test str method"""
        u = User()
        u.id = "12345"
        self.assertIn("[User] (12345)", u.__str__())
        self.assertIn("'id': '12345'", u.__str__())

    def test_save(self):
        """test save"""
        u = User()
        sleep(0.05)
        first_save = u.updated_at
        u.save()
        self.assertLess(first_save, u.updated_at)

    def test_to_dict(self):
        """test dictionary in User class"""
        u = User()
        self.assertIn("id", u.to_dict())
        self.assertIn("created_at", u.to_dict())
        self.assertIn("updated_at", u.to_dict())
        self.assertIn("__class__", u.to_dict())


if __name__ == "__main__":
    unittest.main()
