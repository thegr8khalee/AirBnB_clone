#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

if __name__ == "__main__":
    unittest.main()