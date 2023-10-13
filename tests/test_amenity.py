#!/usr/bin/python3
"""
Imported modules:
uuid
time, datetime
BaseModel, Amenity, User
"""
import time
import uuid
import datetime
import unittest
from models.user import User
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Testcases for models state
    Below tests check if the attributes of the state class
    are of the correct type
    """
    @classmethod
    def setUp(cls):
        """
        Initialize instances that will be used for tests
        Params:
            state - used in testcases for inherited basemodel atributes
            state1 - used in testcases for class Amenity attributes
        """
        cls.amenity = Amenity()
        cls.amenity1 = Amenity()

    @classmethod
    def tearDown(cls):
        """ Cleanup test instances after use"""
        del cls.amenity
        del cls.amenity1

    def test_amenity_id(self):
        """Test if amenity id is a string"""
        self.assertIsInstance(self.amenity.id, str)

    def test_amenity_created_at(self):
        """ Test if value stored for instance is of type datetime """
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)

    def test_amenity_updated_at(self):
        """ updated_at value should be of type datetime """
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)

    def test_amenity_instance(self):
        """
        Instantiaon of the of the Amenity class should be of type Amenity class
        """
        self.assertEqual(type(self.amenity), Amenity)

    def test_name(self):
        """ name should be a string"""
        self.assertIsInstance(self.amenity1.name, str)

    def test_subclass(self):
        """ Test if Amenity is a subclass of BaseModel"""
        self.assertEqual(issubclass(Amenity, BaseModel), True)


class TestAmenityAttributes(unittest.TestCase):
    """
    Tests if the new() and update() defined in file_storage.py are working
    with the Amenity class
    """

    def test_new(self):
        """
        Tests if a new attribute can be created and stored correctly by
        calling save
        """
        self.amenity2 = Amenity()
        self.amenity2.name = "Brian"
        amenityDict = self.amenity2.to_dict()
        self.amenity2.save()
        self.assertIsInstance(self.amenity2, Amenity)
        self.assertEqual(self.amenity2.name, "Brian")
        self.assertEqual(type(amenityDict), dict)

    def test_update(self):
        """ Test if existing attributes are correctly updated """
        self.amenity3 = Amenity()
        self.amenity3.first_name = "Emma"
        self.amenity3.email = "omondiibrian00@gmail.com"
        self.assertEqual(self.amenity3.first_name, "Emma")
        self.assertEqual(self.amenity3.email, "omondiibrian00@gmail.com")
        self.assertLess(self.amenity3.created_at, self.amenity3.updated_at)


if __name__ == '__main__':
    unittest.main()
