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
        review_json = open('../../data/review.json')
        # review_json = open('test/data/review.json')
        self.review_from_query = json.load(review_json)
        review_json.close()
        self.manage_reviews = ManageReviews()
        self.manage_reviews.get_user = MagicMock(return_value=Review(self.review_from_query[0]))
        self.manage_reviews.get_reviews_by_book = MagicMock(return_value=Review(self.review_from_query[0]))

    def test_create_new(self):
        new_review = self.manage_reviews.create_new('60773a16cb838494e13d3652', '608f2e4ba54d753c4466305f', 3,
                                                    "awesome books")
        self.assertIsNotNone(new_review)
