#!/usr/bin/python3
"""
Testing stotage storage
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        self.assertEqual(self.storage.all(), {})
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(self.storage.all(), {"BaseModel.{}".format(obj.id): obj})

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

    def test_save_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        self.assertIn("BaseModel.{}".format(obj.id), new_storage.all())

if __name__ == '__main__':
    unittest.main()
