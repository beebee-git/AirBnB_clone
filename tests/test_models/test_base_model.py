#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
from datetime import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """Testing base model"""

    @classmethod
    def setUp(test_cls):
        try:
            os.rename("file.json", "tmp_file")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        test_cls.storage = FileStorage()
        test_cls.base = BaseModel()

    @classmethod
    def tearDownClass(test_cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp_file", "file.json")
        except IOError:
            pass
        del test_cls.storage
        del test_cls.base

    def test_method(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "delete"))

    def test_attributes(self):
        self.assertEqual(datetime, type(self.base.created_at))
        self.assertEqual(datetime, type(self.base.updated_at))
        self.assertEqual(str, type(self.base.id))

    def test_two_models(self):
        new_base = BaseModel()
        self.assertNotEqual(self.base.id, new_base.id)
        self.assertLess(self.base.created_at, new_base.created_at)
        self.assertLess(self.base.updated_at, new_base.updated_at)

    def test_to_dict(self):
        new_base = self.base.to_dict()
        self.assertEqual(dict, type(new_base))
        self.assertEqual(self.base.id, new_base["id"])
        self.assertEqual("BaseModel", new_base["__class__"])
        self.assertEqual(self.base.created_at.isoformat(), new_base["created_at"])
        self.assertEqual(self.base.updated_at.isoformat(), new_base["updated_at"])
        self.assertEqual(new_base.get("_sa_instance_state", None), None)


    @unittest.skipIf(os.getenv("HBNB_ENV") is not None, "Testing DBStorage")
    def test_save(self):
        new_base = self.base.updated_at
        self.base.save()
        self.assertLess(new_base, self.base.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("BaseModel.{}".format(self.base.id), file.read())


if __name__ == "__main__":
    unittest.main()
