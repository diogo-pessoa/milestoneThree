import json
import unittest
from unittest.mock import MagicMock

from app import get_app_with_config
from config import TestConfig
from src.bookshelf.manage_reviews.manage_reviews import ManageReviews
from src.bookshelf.review import Review

app, mongo = get_app_with_config(TestConfig)


class ManageReviewTest(unittest.TestCase):

    def setUp(self):
        review_json = open('test/data/review.json')
        self.review_from_query = json.load(review_json)
        review_json.close()
        reviews = []
        self.manage_reviews = ManageReviews()
        for review in self.review_from_query:
            reviews.append(Review(review))
        self.manage_reviews.get_many = MagicMock(return_value=reviews)

    def test_get_rate_by_book_id(self):
        """
          expect to get the average rate of books returned from DB
        """
        book_rates = self.manage_reviews.get_rate_by_book_id('qwdsmnf1jh1231')
        self.assertEqual(4, book_rates)

    def test_delete_review_by_id_ok(self):
        """
        Expect to return flash_message is object is deleted
        """
        self.manage_reviews.delete = MagicMock(return_value=None)
        delete_review = self.manage_reviews.delete_review_by_id('607c901da54d752ec8613324')
        self.assertEqual("Review deleted successfully.", delete_review['flash_message'])

    def test_create_new_review(self):
        """
            Expect to return flash_message when new review is created
        """
        self.manage_reviews.create = MagicMock(return_value=None)
        user_input_dict = self.review_from_query[0]
        create_review = self.manage_reviews.add_new_review(user_input_dict['book_id'], user_input_dict['reviewer_id'],
                                                           user_input_dict['rate'], user_input_dict['feedback'])
        self.assertEqual("Review created successfully.", create_review['flash_message'])

    def test_create_new_review_create_fails(self):
        """
            Expect to return flash_message with error if create response is not None
        """
        self.manage_reviews.create = MagicMock(return_value="Error")
        user_input_dict = self.review_from_query[0]
        create_review = self.manage_reviews.add_new_review(user_input_dict['book_id'], user_input_dict['reviewer_id'],
                                                           user_input_dict['rate'], user_input_dict['feedback'])
        self.assertEqual("Could Not create review, Try Again", create_review['flash_message'])
