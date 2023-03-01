#!/usr/bin/python3
import unittest
from models.state import State

class Test_attributes_methods_State(unittest.TestCase):
    def test_name(self):
        state = State()
        self.assertTrue(not state.name)
        self.assertTrue(type(state.name) == str)
