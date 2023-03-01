#!/usr/bin/python3
import unittest
from models.city import City


class Test_City(unittest.TestCase):
    def test_state_id(self):
        city = City()
        self.assertTrue(not city.name)
        self.assertTrue(type(city.name) == str)

    def test_name(self):
        city = City()
        self.assertTrue(not city.name)
        self.assertTrue(type(city.name) == str)
