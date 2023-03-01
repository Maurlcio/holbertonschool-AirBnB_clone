#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    def test_name(self):
        amenity = Amenity()
        self.assertTrue(not amenity.name)
        self.assertTrue(type(amenity.name) == str)
