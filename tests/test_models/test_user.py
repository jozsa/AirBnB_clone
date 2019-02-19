#!/usr/bin/python3
<<<<<<< HEAD
"""Unittest for class User
=======
"""Unittest for class BaseModel
>>>>>>> 8baeda7f36de82e4a62610ed57b4bc0f7f8208a5
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
<<<<<<< HEAD
from models.user import User


class TestUser(unittest.TestCase):
    """Testing User"""
    def setUp(self):
        """
        Create a new instance of User before each test
        """
        self.u1 = User()

    def tearDown(self):
        """
        Delete User instance before next test
        """
        del self.u1
=======


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
>>>>>>> 8baeda7f36de82e4a62610ed57b4bc0f7f8208a5

    def test_uniqueUUID(self):
        """
        Make sure each UUID is unique
        """
<<<<<<< HEAD
        u2 = User()
        self.assertNotEqual(self.u1.id, u2.id)
=======
        b2 = BaseModel()
        self.assertNotEqual(self.b1.id, b2.id)
>>>>>>> 8baeda7f36de82e4a62610ed57b4bc0f7f8208a5

    def test_id_type(self):
        """
        Make sure id is a string not uuid data type
        """
<<<<<<< HEAD
        self.assertEqual(type(self.u1.id), str)
=======
        self.assertEqual(type(self.b1.id), str)
>>>>>>> 8baeda7f36de82e4a62610ed57b4bc0f7f8208a5

    def test_created_at_type(self):
        """
        Make sure created_at is datetime data type
        """
<<<<<<< HEAD
        self.assertEqual(type(self.u1.created_at), datetime)
=======
        self.assertEqual(type(self.b1.created_at), datetime)
>>>>>>> 8baeda7f36de82e4a62610ed57b4bc0f7f8208a5

    def test_updated_at_type(self):
        """
        Make sure updated_at is datetime data type
        """
<<<<<<< HEAD
        self.assertEqual(type(self.u1.updated_at), datetime)

    def test_email_type(self):
        """
        Make sure email is str data type
        """
        self.assertEqual(type(User.email), str)

    def test_password_type(self):
        """
        Make sure password is str data type
        """
        self.assertEqual(type(User.password), str)

    def test_first_name_type(self):
        """
        Make sure first_name is str data type
        """
        self.assertEqual(type(User.first_name), str)

    def test_last_name_type(self):
        """
        Make sure last_name is str data type
        """
        self.assertEqual(type(User.last_name), str)
=======
        self.assertEqual(type(self.b1.updated_at), datetime)
>>>>>>> 8baeda7f36de82e4a62610ed57b4bc0f7f8208a5

    def test_save(self):
        """
        Make sure save does update the updated_at attribute
        """
<<<<<<< HEAD
        old_updated_at = self.u1.updated_at
        self.u1.save()
        self.assertNotEqual(old_updated_at, self.u1.updated_at)
=======
        old_updated_at = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(old_updated_at, self.b1.updated_at)
>>>>>>> 8baeda7f36de82e4a62610ed57b4bc0f7f8208a5

    def test_str(self):
        """
        Testing return of __str__
        """
<<<<<<< HEAD
        self.assertEqual(str(self.u1), "[User] ({}) {}".
                         format(self.u1.id, self.u1.__dict__))
=======
        self.assertEqual(str(self.b1), "[BaseModel] ({}) {}".
                         format(self.b1.id, self.b1.__dict__))
>>>>>>> 8baeda7f36de82e4a62610ed57b4bc0f7f8208a5

    def test_to_dict(self):
        """
        Make sure to_dict returns the right dictionary
        and the dict has the right attributes with the right types.
        """
<<<<<<< HEAD
        model_json = self.u1.to_dict()
=======
        model_json = self.b1.to_dict()
>>>>>>> 8baeda7f36de82e4a62610ed57b4bc0f7f8208a5
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_kwargs(self):
        """
<<<<<<< HEAD
        Test passing kwargs to User instantation
        """
        json_dict = self.u1.to_dict()
        u2 = User(**json_dict)
        self.assertEqual(self.u1.id, u2.id)
        self.assertEqual(self.u1.created_at, u2.created_at)
        self.assertEqual(self.u1.updated_at, u2.updated_at)
        self.assertNotEqual(self.u1, u2)
=======
        Test passing kwargs to BaseModel instantation
        """
        json_dict = self.b1.to_dict()
        b2 = BaseModel(**json_dict)
        self.assertEqual(self.b1.id, b2.id)
        self.assertEqual(self.b1.created_at, b2.created_at)
        self.assertEqual(self.b1.updated_at, b2.updated_at)
        self.assertNotEqual(self.b1, b2)
>>>>>>> 8baeda7f36de82e4a62610ed57b4bc0f7f8208a5
