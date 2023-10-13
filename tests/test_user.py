#!/usr/bin/python3
"""
Imported modules:
uuid
time, datetime
BaseModel, User
"""
import time
import uuid
import datetime
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Testcases for models user
    Below tests check if the attributes of the user class
    are of the correct type
    """
    @classmethod
    def setUp(cls):
        """
        Initialize instances that will be used for tests
        Params:
            user - used in testcases for inherited basemodel atributes
            user1 - used in testcases for class User attributes
        """
        cls.user = User()
        cls.user1 = User()

    @classmethod
    def tearDown(cls):
        """ Cleanup test instances after use"""
        del cls.user
        del cls.user1

    def test_user_id(self):
        """Test if user id is a string"""
        self.assertIsInstance(self.user.id, str)

    def test_user_created_at(self):
        """ Test if value stored for instance is of type datetime """
        self.assertIsInstance(self.user.created_at, datetime.datetime)

    def test_user_updated_at(self):
        """ updated_at value should be of type datetime """
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

    def test_user_instance(self):
        """
        Instantiaon of the of the User class should be of type User class
        """
        self.assertEqual(type(self.user), User)

    def test_email(self):
        """email should always be a string"""
        self.assertIsInstance(self.user1.email, str)

    def test_password(self):
        """ password should store string type objects """
        self.assertIsInstance(self.user1.password, str)

    def test_first_name(self):
        """ first_name should store a string """
        self.assertIsInstance(self.user1.first_name, str)

    def test_last_name(self):
        """ last_name should be a string"""
        self.assertIsInstance(self.user1.last_name, str)

    def test_subclass(self):
        """ Test if User is a subclass of BaseModel"""
        self.assertEqual(issubclass(User, BaseModel), True)


class TestUserAttributes(unittest.TestCase):
    """
    Tests if the new() and update() defined in file_storage.py are working
    with the User class

    @classmethod
    def setUp(self):
         Initialize instances that will be used for tests
        cls.user2 = User()
        cls.user3 = User()

    def tearDown(self):
        Del test instances setup earlier from memory
        del cls.user2
        del cls.user3
   """

    def test_new(self):
        """
        Tests if a new attribute can be created and stored correctly by
        calling save
        """
        self.user2 = User()
        self.user2.name = "Brian"
        userDict = self.user2.to_dict()
        self.user2.save()
        self.assertIsInstance(self.user2, User)
        self.assertEqual(self.user2.name, "Brian")
        self.assertEqual(type(userDict), dict)

    def test_update(self):
        """ Test if existing attributes are correctly updated """
        self.user3 = User()
        self.user3.first_name = "Emma"
        self.user3.email = "omondiibrian00@gmail.com"
        self.assertEqual(self.user3.first_name, "Emma")
        self.assertEqual(self.user3.email, "omondiibrian00@gmail.com")
        self.assertLess(self.user3.created_at, self.user3.updated_at)


if __name__ == '__main__':
    unittest.main()
