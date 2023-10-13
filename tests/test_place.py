#!/usr/bin/python3
"""
Imported modules:
uuid
time, datetime
BaseModel, User, Place
"""
import time
import uuid
import datetime
import unittest
from models.user import User
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Testcases for models place
    Below tests check if the attributes of the place class
    are of the correct type
    """
    @classmethod
    def setUp(cls):
        """
        Initialize instances that will be used for tests
        Params:
            place - used in testcases for inherited basemodel atributes
            place1 - used in testcases for class Place attributes
        """
        cls.place = Place()
        cls.place1 = Place()

    @classmethod
    def tearDown(cls):
        """ Cleanup test instances after use"""
        del cls.place
        del cls.place1

    def test_place_id(self):
        """Test if place id is a string"""
        self.assertIsInstance(self.place.id, str)

    def test_place_created_at(self):
        """ Test if value stored for instance is of type datetime """
        self.assertIsInstance(self.place.created_at, datetime.datetime)

    def test_place_updated_at(self):
        """ updated_at value should be of type datetime """
        self.assertIsInstance(self.place.updated_at, datetime.datetime)

    def test_place_instance(self):
        """
        Instantiaon of the of the Place class should be of type Place class
        """
        self.assertEqual(type(self.place), Place)

    def test_city_id(self):
        """email should always be a string"""
        self.assertIsInstance(self.place1.city_id, str)

    def test_user_id(self):
        """ user_id should store string type objects """
        self.assertIsInstance(self.place1.user_id, str)

    def test_name(self):
        """ name should store a string """
        self.assertIsInstance(self.place1.name, str)

    def test_description(self):
        """ description should be a string"""
        self.assertIsInstance(self.place1.description, str)

    def test_number_rooms(self):
        """ number_rooms should be a string"""
        self.assertIsInstance(self.place1.number_rooms, int)

    def test_number_bathrooms(self):
        """ number_rooms should be a string"""
        self.assertIsInstance(self.place1.number_bathrooms, int)

    def test_max_guest(self):
        """ max_guest should be a string"""
        self.assertIsInstance(self.place1.max_guest, int)

    def test_price_by_night(self):
        """ price_by_night should be a string"""
        self.assertIsInstance(self.place1.price_by_night, int)

    def test_latitude(self):
        """ latitude should be a string"""
        self.assertIsInstance(self.place1.latitude, float)

    def test_longitude(self):
        """ longitude should be a string"""
        self.assertIsInstance(self.place1.longitude, float)

    def test_amenity_ids(self):
        """ amenity_ids should be a string"""
        self.assertIsInstance(self.place1.amenity_ids, list)

    def test_subclass(self):
        """ Test if Place is a subclass of BaseModel"""
        self.assertEqual(issubclass(Place, BaseModel), True)


class TestPlaceAttributes(unittest.TestCase):
    """
    Tests if the new() and update() defined in file_storage.py are working
    with the Place class

    @classmethod
    def setUp(self):
         Initialize instances that will be used for tests
        cls.place2 = Place()
        cls.place3 = Place()

    def tearDown(self):
        Del test instances setup earlier from memory
        del cls.place2
        del cls.place3
   """

    def test_new(self):
        """
        Tests if a new attribute can be created and stored correctly by
        calling save
        """
        self.place2 = Place()
        self.place2.name = "Brian"
        placeDict = self.place2.to_dict()
        self.place2.save()
        self.assertIsInstance(self.place2, Place)
        self.assertEqual(self.place2.name, "Brian")
        self.assertEqual(type(placeDict), dict)

    def test_update(self):
        """ Test if existing attributes are correctly updated """
        self.place3 = Place()
        self.place3.first_name = "Emma"
        self.place3.email = "omondiibrian00@gmail.com"
        self.assertEqual(self.place3.first_name, "Emma")
        self.assertEqual(self.place3.email, "omondiibrian00@gmail.com")
        self.assertLess(self.place3.created_at, self.place3.updated_at)


if __name__ == '__main__':
    unittest.main()
