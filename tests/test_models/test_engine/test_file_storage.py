#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up a clean environment before each test."""
        self.storage = FileStorage()
        self.obj = BaseModel()

    def tearDown(self):
        """Clean up the environment after each test."""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        """Test the all method."""
        # Add the object to the storage
        self.storage.new(self.obj)

        # Check if all objects are returned correctly
        all_objects = self.storage.all()
        self.assertIn("BaseModel." + self.obj.id, all_objects)

    def test_new(self):
        """Test the new method."""
        # Add the object to the storage
        self.storage.new(self.obj)

        # Check if the object is added correctly
        self.assertIn("BaseModel." + self.obj.id, self.storage.all())

    def test_save(self):
        """Test the save method."""
        # Add the object to the storage
        self.storage.new(self.obj)

        # Save the object to the JSON file
        self.storage.save()

        # Check if the JSON file exists
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

        # Check if the contents of the JSON file are correct
        with open(self.storage._FileStorage__file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.assertIn("BaseModel." + self.obj.id, data)

    def test_reload(self):
        """Test the reload method."""
        # Add the object to the storage
        self.storage.new(self.obj)

        # Save the object to the JSON file
        self.storage.save()

        # Clear objects from the storage
        self.storage._FileStorage__objects = {}

        # Reload objects from the JSON file
        self.storage.reload()

        # Check if the object is reloaded correctly
        self.assertIn("BaseModel." + self.obj.id, self.storage.all())

if __name__ == '__main__':
    unittest.main()
