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
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Testcases for models review
    Below tests check if the attributes of the review class
    are of the correct type
    """
    @classmethod
    def setUp(cls):
        """
        Initialize instances that will be used for tests
        Params:
            review - used in testcases for inherited basemodel atributes
            review1 - used in testcases for class Review attributes
        """
        cls.review = Review()
        cls.review1 = Review()

    @classmethod
    def tearDown(cls):
        """ Cleanup test instances after use"""
        del cls.review
        del cls.review1

    def test_review_id(self):
        """Test if review id is a string"""
        self.assertIsInstance(self.review.id, str)

    def test_review_created_at(self):
        """ Test if value stored for instance is of type datetime """
        self.assertIsInstance(self.review.created_at, datetime.datetime)

    def test_review_updated_at(self):
        """ updated_at value should be of type datetime """
        self.assertIsInstance(self.review.updated_at, datetime.datetime)

    def test_review_instance(self):
        """
        Instantiaon of the of the Review class should be of type Review class
        """
        self.assertEqual(type(self.review), Review)

    def test_user_id(self):
        """ review should be a string"""
        self.assertIsInstance(self.review1.user_id, str)

    def test_text(self):
        """ review should be a string"""
        self.assertIsInstance(self.review1.text, str)

    def test_place_id(self):
        """ place_id should be a string"""
        self.assertIsInstance(self.review1.place_id, str)

    def test_subclass(self):
        """ Test if Review is a subclass of BaseModel"""
        self.assertEqual(issubclass(Review, BaseModel), True)


class TestReviewAttributes(unittest.TestCase):
    """
    Tests if the new() and update() defined in file_storage.py are working
    with the Review class
    """

    def test_new(self):
        """
        Tests if a new attribute can be created and stored correctly by
        calling save
        """
        self.review2 = Review()
        self.review2.name = "Brian"
        reviewDict = self.review2.to_dict()
        self.review2.save()
        self.assertIsInstance(self.review2, Review)
        self.assertEqual(self.review2.name, "Brian")
        self.assertEqual(type(reviewDict), dict)

    def test_update(self):
        """ Test if existing attributes are correctly updated """
        self.review3 = Review()
        self.review3.first_name = "Emma"
        self.review3.email = "omondiibrian00@gmail.com"
        self.assertEqual(self.review3.first_name, "Emma")
        self.assertEqual(self.review3.email, "omondiibrian00@gmail.com")
        self.assertLess(self.review3.created_at, self.review3.updated_at)


if __name__ == '__main__':
    unittest.main()
