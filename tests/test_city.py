#!/usr/bin/python3
"""
Imported modules:
uuid
time, datetime
BaseModel, City, User
"""
import time
import uuid
import datetime
import unittest
from models.user import User
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Testcases for models city
    Below tests check if the attributes of the city class
    are of the correct type
    """
    @classmethod
    def setUp(cls):
        """
        Initialize instances that will be used for tests
        Params:
            city - used in testcases for inherited basemodel atributes
            city1 - used in testcases for class City attributes
        """
        cls.city = City()
        cls.city1 = City()

    @classmethod
    def tearDown(cls):
        """ Cleanup test instances after use"""
        del cls.city
        del cls.city1

    def test_city_id(self):
        """Test if city id is a string"""
        self.assertIsInstance(self.city.id, str)

    def test_city_created_at(self):
        """ Test if value stored for instance is of type datetime """
        self.assertIsInstance(self.city.created_at, datetime.datetime)

    def test_city_updated_at(self):
        """ updated_at value should be of type datetime """
        self.assertIsInstance(self.city.updated_at, datetime.datetime)

    def test_city_instance(self):
        """
        Instantiaon of the of the City class should be of type City
        class
        """
        self.assertEqual(type(self.city), City)

    def test_name(self):
        """ name should be a string"""
        self.assertIsInstance(self.city1.name, str)

    def test_state_id(self):
        """ name should be a string"""
        self.assertIsInstance(self.city1.state_id, str)

    def test_subclass(self):
        """ Test if City is a subclass of BaseModel"""
        self.assertEqual(issubclass(City, BaseModel), True)


class TestCityAttributes(unittest.TestCase):
    """
    Tests if the new() and update() defined in file_storage.py are working
    with the City class
    """

    def test_new(self):
        """
        Tests if a new attribute can be created and stored correctly by
        calling save
        """
        self.city2 = City()
        self.city2.name = "Brian"
        cityDict = self.city2.to_dict()
        self.city2.save()
        self.assertIsInstance(self.city2, City)
        self.assertEqual(self.city2.name, "Brian")
        self.assertEqual(type(cityDict), dict)

    def test_update(self):
        """ Test if existing attributes are correctly updated """
        self.city3 = City()
        self.city3.first_name = "Emma"
        self.city3.email = "omondiibrian00@gmail.com"
        self.assertEqual(self.city3.first_name, "Emma")
        self.assertEqual(self.city3.email, "omondiibrian00@gmail.com")
        self.assertLess(self.city3.created_at, self.city3.updated_at)


if __name__ == '__main__':
    unittest.main()
