import json
import unittest
from unittest.mock import MagicMock

from app import get_app_with_config
from config import TestConfig
from src.bookshelf.manage_reviews.manage_reviews import ManageReviews
from src.bookshelf.review import Review

app, mongo = get_app_with_config(TestConfig)


class NewReviewTest(unittest.TestCase):

    def setUp(self):
        # Mock of Review Query
        review_json = open('../../data/review.json')
        # review_json = open('test/data/review.json')
        review_from_query = json.load(review_json)
        reviews = []
        self.manage_reviews = ManageReviews()
        for review in review_from_query:
            reviews.append(Review(review))
        self.manage_reviews.get_reviews = MagicMock(return_value=reviews)

    def test_get_rate_by_book_id(self):
        """
          expect to get the average rate of books returned from DB
        """
        book_rates = self.manage_reviews.get_rate_by_book_id('qwdsmnf1jh1231')
        self.assertEqual(4, book_rates)
