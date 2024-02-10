import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_str(self):
        my_model = BaseModel()

        expected_output = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_output)

    def test_save(self):
        my_model = BaseModel()

        last_updated = my_model.updated_at
        current_update = my_model.save()

        self.assertNotEqual(last_updated, current_update)

    def test_dict(self):
        my_model = BaseModel()

        expected_dict = {
            'id': my_model.id,
            '__class__': 'BaseModel',
            'created_at': my_model.created_at.isoformat(),
            'updated_at': my_model.updated_at.isoformat()
        }
        self.assertDictEqual(my_model.to_dict(), expected_dict)

if __name__ == "__main__":
    unittest.main()
