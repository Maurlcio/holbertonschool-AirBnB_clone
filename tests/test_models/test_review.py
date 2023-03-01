#!/usr/bin/python3
import unittest
from models.review import Review


class Test_attributes_methods_Review(unittest.TestCase):
    def test_place_id(self):
        review = Review()
        self.assertTrue(not review.place_id)
        self.assertTrue(type(review.place_id) == str)

    def test_user_id(self):
        review = Review()
        self.assertTrue(not review.user_id)
        self.assertTrue(type(review.user_id) == str)

    def test_text(self):
        review = Review()
        self.assertTrue(not review.text)
        self.assertTrue(type(review.text) == str)
