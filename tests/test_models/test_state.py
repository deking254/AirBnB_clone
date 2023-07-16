#!/usr/bin/python3

"""test module for State class"""
import unittest
from time import sleep
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """tests for class state"""
    def test_no_arg(self):
        """test no argument"""
        self.assertEqual(State, type(State()))

    def test_unique_id(self):
        """test unique id"""
        s = State()
        s1 = State()
        self.assertNotEqual(s, s1)

    def test_created_at(self):
        """test created at"""
        s = State()
        sleep(0.05)
        s1 = State()
        self.assertLess(s.created_at, s1.created_at)

    def test_updated_at(self):
        """test updated at"""
        s = State()
        sleep(0.05)
        s1 = State()
        self.assertLess(s.updated_at, s1.updated_at)

    def test_str(self):
        """test str"""
        s = State()
        s.id = "12345"
        self.assertIn("[State] (12345)", s.__str__())
        self.assertIn("'id': '12345'", s.__str__())

    def test_save(self):
        """test save"""
        s = State()
        sleep(0.05)
        first_save = s.updated_at
        s.save()
        self.assertLess(first_save, s.updated_at)

    def test_to_dict(self):
        """test dictionary method"""
        s = State()
        self.assertIn("id", s.to_dict())
        self.assertIn("created_at", s.to_dict())
        self.assertIn("updated_at", s.to_dict())
        self.assertIn("__class__", s.to_dict())


if __name__ == "__main__":
    unittest.main()
