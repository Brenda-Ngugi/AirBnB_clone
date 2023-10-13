#!/usr/bin/python3
"""
Imported modules:
uuid
time, datetime
BaseModel, State, User
"""
import time
import uuid
import datetime
import unittest
from models.user import User
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
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
            state1 - used in testcases for class State attributes
        """
        cls.state = State()
        cls.state1 = State()

    @classmethod
    def tearDown(cls):
        """ Cleanup test instances after use"""
        del cls.state
        del cls.state1

    def test_state_id(self):
        """Test if state id is a string"""
        self.assertIsInstance(self.state.id, str)

    def test_state_created_at(self):
        """ Test if value stored for instance is of type datetime """
        self.assertIsInstance(self.state.created_at, datetime.datetime)

    def test_state_updated_at(self):
        """ updated_at value should be of type datetime """
        self.assertIsInstance(self.state.updated_at, datetime.datetime)

    def test_state_instance(self):
        """
        Instantiaon of the of the State class should be of type State class
        """
        self.assertEqual(type(self.state), State)

    def test_name(self):
        """ name should be a string"""
        self.assertIsInstance(self.state1.name, str)

    def test_subclass(self):
        """ Test if State is a subclass of BaseModel"""
        self.assertEqual(issubclass(State, BaseModel), True)


class TestStateAttributes(unittest.TestCase):
    """
    Tests if the new() and update() defined in file_storage.py are working
    with the State class
    """

    def test_new(self):
        """
        Tests if a new attribute can be created and stored correctly by
        calling save
        """
        self.state2 = State()
        self.state2.name = "Brian"
        stateDict = self.state2.to_dict()
        self.state2.save()
        self.assertIsInstance(self.state2, State)
        self.assertEqual(self.state2.name, "Brian")
        self.assertEqual(type(stateDict), dict)

    def test_update(self):
        """ Test if existing attributes are correctly updated """
        self.state3 = State()
        self.state3.first_name = "Emma"
        self.state3.email = "omondiibrian00@gmail.com"
        self.assertEqual(self.state3.first_name, "Emma")
        self.assertEqual(self.state3.email, "omondiibrian00@gmail.com")
        self.assertLess(self.state3.created_at, self.state3.updated_at)


if __name__ == '__main__':
    unittest.main()
