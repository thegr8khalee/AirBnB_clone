import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def test_init_with_args_kwargs(self):
        now = datetime.utcnow()
        data = {
            "id": "test-id",
            "created_at": now.isoformat(),
            "updated_at": now.isoformat(),
            "name": "Test",
            "my_number": 42
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, "test-id")
        self.assertEqual(model.created_at, now)
        self.assertEqual(model.updated_at, now)
        self.assertEqual(model.name, "Test")
        self.assertEqual(model.my_number, 42)

    def test_str_method(self):
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        current = model.save()
        self.assertNotEqual(initial_updated_at, current)

    def test_to_dict_method(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
