import json
import unittest

from src.bookshelf.book import Book


class ReviewTest(unittest.TestCase):

    def setUp(self):
        file = open('test/data/book.json')
        book_data = json.load(file)
        file.close()
        self.books = []
        for book in book_data:
            self.books.append(Book(book))

    def test_get_object_dict(self):
        book = self.books[0].get_dict()
        self.assertEqual("MockBook", book['title'])
        self.assertEqual("Jon Doe", book['author'])
        self.assertTrue(book['reviewed'])

    def test_get_reviewed_returns_false(self):
        book = self.books[1].get_dict()
        self.assertFalse(book['reviewed'])


if __name__ == "__main__":
    unittest.main()
