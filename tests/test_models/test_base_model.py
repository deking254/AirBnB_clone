#!/usr/bin/python3

"""Test module for base_model"""
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """unittests for basemodel"""
    def setUp(self):
        """instantiate class"""
        self.bm = BaseModel()

    def test_no_args(self):
        """test no argument passed"""
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "id"))
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertTrue(hasattr(bm1, "updated_at"))

    def test_unique_id(self):
        """Test unique ids"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_base_type(self):
        """test type of basemodel"""
        self.assertEqual(type(BaseModel()), BaseModel)

    def test_created_at(self):
        """test creation of object"""
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_updated_at(self):
        """test update of object"""
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str(self):
        """test string representation method"""
        bm1 = BaseModel()
        bm1.id = "12345"
        bm1.name = "John Doe"

        self.assertIn("[BaseModel] (12345)", bm1.__str__())
        self.assertIn("'id': '12345'", bm1.__str__())

    def test_dict_attr(self):
        """test dictionary attribute"""
        bm1 = BaseModel()
        bm1.name = "John Doe"
        bm1.age = 25
        obj_dict = bm1.to_dict()
        self.assertIn('name', obj_dict)
        self.assertEqual(obj_dict['name'], 'John Doe')
        self.assertIn('age', obj_dict)
        self.assertEqual(obj_dict['age'], 25)

    def test_id_is_string(self):
        """test id is string"""
        bm1 = BaseModel()
        self.assertIsInstance(bm1.id, str)

    def test_dict_has_class_name(self):
        """test class name in dictionary"""
        bm1 = BaseModel()
        obj_dict = bm1.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_save_model(self):
        """test save method"""
        bm1 = BaseModel()
        prev_updated_at = bm1.updated_at
        bm1.save()
        first_save = bm1.updated_at
        bm1.save()
        second_save = bm1.updated_at
        self.assertLess(first_save, second_save)
        sleep(0.05)
        bm1.save()
        self.assertNotEqual(second_save, first_save)
        self.assertNotEqual(bm1.updated_at, prev_updated_at)

    def test_deserialization(self):
        """test deserialization of object"""
        bm1 = BaseModel()
        bm1.name = 'John Doe'
        bm1.age = 25
        obj_dict = bm1.to_dict()

        new_instance = BaseModel(**obj_dict)
        self.assertEqual(new_instance.name, 'John Doe')
        self.assertEqual(new_instance.age, 25)

    def test_serialization(self):
        """test serialization of obj"""
        bm1 = BaseModel()
        bm1.id = "12345"
        bm1.name = "John Doe"
        serialized_data = bm1.to_dict()
        self.assertIsInstance(serialized_data, dict)
        self.assertEqual(serialized_data['__class__'], 'BaseModel')
        self.assertEqual(serialized_data['id'], '12345')
        self.assertEqual(serialized_data['name'], 'John Doe')


if __name__ == "__main__":
    unittest.main()
