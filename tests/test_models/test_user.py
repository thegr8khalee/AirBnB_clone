#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_instance(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_inheritance(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_str_representation(self):
        user = User()
        expected_output = f"[User] ({user.id}) {user.__dict__}"
        self.assertEqual(str(user), expected_output)

    def test_to_dict_method(self):
        user = User()
        user_dict = user.to_dict()
        expected_keys = ["id", "email", "password", "first_name", "last_name", "__class__", "created_at", "updated_at"]
        self.assertCountEqual(user_dict.keys(), expected_keys)
        self.assertEqual(user_dict['__class__'], 'User')

if __name__ == "__main__":
    unittest.main()