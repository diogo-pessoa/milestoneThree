import json
import unittest

from src.bookshelf.review import Review


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
        """
        Test review __init__ fields are populated properly
        """
        review = self.review[0].get_dict()
        self.assertIsNotNone(review['reviewer_id'])
        self.assertIsNotNone(review['book_id'])
        self.assertEqual(4, review['rate'])

    def test_set_reviewer(self):
        """
        Expect Setter to update reviewer name value

        """
        review = self.review[0]
        self.assertEqual("", review.get_reviewer())
        review.set_reviewer_name("Name")
        self.assertEqual("Name", review.get_reviewer())

    def test_set_book_title(self):
        """
        Expect to set a book_title on existing review object

        """
        review = self.review[0]
        self.assertEqual("", review.get_book_title())
        review.set_book_title("Book Title")
        self.assertEqual("Book Title", review.get_book_title())


if __name__ == "__main__":
    unittest.main()
