#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    def test_review_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_instance(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

if __name__ == "__main__":
    unittest.main()