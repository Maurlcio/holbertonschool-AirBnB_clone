#!/usr/bin/ptyhon3
"""" Tests for the file user.py """
import unittest
from models.user import User


class Test_attributes_methods_User(unittest.TestCase):
    def test_email(self):
        user = User()
        self.assertTrue(not user.email)
        self.assertTrue(type(user.email) == str)

    def test_password(self):
        user = User()
        self.assertTrue(not user.password)
        self.assertTrue(type(user.password) == str)

    def test_first_name(self):
        user = User()
        self.assertTrue(not user.first_name)
        self.assertTrue(type(user.first_name) == str)


    def test_last_name(self):
        user = User()
        self.assertTrue(not user.last_name)
        self.assertTrue(type(user.last_name) == str)
