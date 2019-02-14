#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
import uuid as uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Testing BaseModel"""
    def setUp(self):
        """
        Create a new instance of BaseModel before each test
        """
        self.b1 = BaseModel()

    def tearDown(self):
        """
        Delete BaseModel instance before next test
        """
        del self.b1

    def test_uniqueUUID(self):
        """
        Make sure each UUID is unique
        """
        b2 = BaseModel()
        self.assertNotEqual(self.b1.id, b2.id)

    def test_id_type(self):
        """
        Make sure id is a string not uuid data type
        """
        self.assertEqual(type(self.b1.id), str)

    def test_created_at_type(self):
        """
        Make sure created_at is datetime data type
        """
        self.assertEqual(type(self.b1.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure updated_at is datetime data type
        """
        self.assertEqual(type(self.b1.updated_at), datetime)
