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
        self.assertEqual("mock-book", book['title'])
        self.assertEqual("Jon Doe", book['author'])
        self.assertTrue(book['reviewed'])

    def test_get_reviewed_returns_false(self):
        book = self.books[1].get_dict()
        self.assertFalse(book['reviewed'])

    def test_raw_title(self):
        book1 = self.books[0].get_title_for_url()
        book3 = self.books[2].get_title_for_url()
        self.assertEqual("mock-book", book1)
        self.assertEqual("the-man-who-mistook-his-wife-for-a-hat", book3)

    def test_get_formatted_title(self):
        book = self.books[0]
        book2 = self.books[1]
        self.assertEqual("Mock Book", book.get_formatted_title())
        self.assertEqual("How To Kill A Mockingbird", book2.get_formatted_title())

    def test_set_title(self):
        book3 = self.books[2]
        new_title = "Lord of the flies"
        book3.set_title_for_url(new_title)
        self.assertEqual("lord-of-the-flies", book3.get_title_for_url())
        self.assertEqual("Lord Of The Flies", book3.get_formatted_title())

    def test_set_title_with_None(self):
        book3 = self.books[2]
        new_title = None
        book3.set_title_for_url(new_title)
        self.assertIsNotNone(book3.get_title_for_url())

    def test_set_title_with_empty_value(self):
        book3 = self.books[2]
        book3.set_title_for_url("")
        self.assertTrue(len(book3.get_title_for_url()) > 0)

    def test_set_title_with_multiple_spaces(self):
        book3 = self.books[2]
        book3.set_title_for_url("Lord of   the flies")
        self.assertEqual("Lord Of   The Flies", book3.get_formatted_title())


if __name__ == "__main__":
    unittest.main()
