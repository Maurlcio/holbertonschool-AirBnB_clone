#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    def test_save(self):
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(old_updated_at, bm.updated_at)

    def test_save_2(self):
        bm = BaseModel()
        bm.save()
        with open('file.json') as file:
            self.assertIn(f"{bm.__class__.__name__}.{bm.id}", file.read())

    def test_to_dict(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertTrue('__class__' in bm_dict)
        self.assertTrue('id' in bm_dict)
        self.assertTrue('created_at' in bm_dict)
        self.assertTrue('updated_at' in bm_dict)

    def test_str(self):
        bm = BaseModel()
        bm_str = str(bm)
        self.assertIsInstance(bm_str, str)
        self.assertIn("[BaseModel]", bm_str)
        self.assertIn("id", bm_str)
        self.assertIn("created_at", bm_str)
        self.assertIn("updated_at", bm_str)

    def test_created_at(self):
        bm = BaseModel()
        creation_bm = bm.created_at
        self.assertTrue(creation_bm == bm.created_at)

if __name__ == "__main__":
    unittest.main()
