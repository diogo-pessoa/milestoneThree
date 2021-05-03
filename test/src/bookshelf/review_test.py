import json
import unittest

from src.bookshelf.review import Review
from src.bookshelf.user import User


class ReviewTest(unittest.TestCase):

    def setUp(self):
        file = open('test/data/review.json')
        review_data = json.load(file)
        file.close()
        reviews = []
        for review in review_data:
            reviews.append(Review(review))
        self.review = reviews

    def test_get_object_dict(self):
        review = self.review[0].get_dict()
        self.assertEqual("willfarnaby", review['reviewer'])
        self.assertEqual("Book1", review['book'])
        self.assertEqual("Book1", review['book'])
        self.assertEqual("4", review['rate'])

if __name__ == "__main__":
    unittest.main()
