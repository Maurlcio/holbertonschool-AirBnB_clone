#!/usr/bin/python3
"""Tests on Place class"""
import unittest
from models.place import Place


class Test_attributes_methods_Place(unittest.TestCase):
    def test_city_id(self):
        t_place = Place()
        self.assertTrue(not t_place.name)
        self.assertTrue(type(t_place.name) is str)

    def test_user_id(self):
        place = Place()
        self.assertTrue(not place.name)
        self.assertTrue(type(place.name) == str)

    def test_name(self):
        place = Place()
        self.assertTrue(not place.name)
        self.assertTrue(type(place.name) == str)

    def test_description(self):
        place = Place()
        self.assertTrue(not place.name)
        self.assertTrue(type(place.name) == str)

    def test_number_rooms(self):
        place = Place()
        self.assertTrue(place.number_rooms == 0)
        self.assertTrue(type(place.number_rooms) is int)

    def test_number_bathrooms(self):
        place = Place()
        self.assertTrue(place.number_bathrooms == 0)
        self.assertTrue(type(place.number_bathrooms) is int)

    def test_max_guest(self):
        place = Place()
        self.assertTrue(place.max_guest == 0)
        self.assertTrue(type(place.max_guest) is int)

    def test_price_by_night(self):
        place = Place()
        self.assertTrue(place.price_by_night == 0)
        self.assertTrue(type(place.price_by_night) is int)

    def test_latitude(self):
        place = Place()
        self.assertTrue(place.latitude == 0.0)
        self.assertTrue(type(place.latitude) is float)

    def test_longitude(self):
        place = Place()
        self.assertTrue(place.longitude == 0.0)
        self.assertTrue(type(place.longitude) is float)

    def test_amenity_ids(self):
        place = Place()
        self.assertTrue(not place.amenity_ids)
        self.assertTrue(type(place.amenity_ids) is list)
