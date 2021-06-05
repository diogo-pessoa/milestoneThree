import json
import unittest
from unittest.mock import MagicMock

from app import get_app_with_config
from config import TestConfig
from src.bookshelf.book import Book
from src.bookshelf.manage_books.manage_books import ManageBooks

app, mongo = get_app_with_config(TestConfig)


class ManageBooksTest(unittest.TestCase):
    def setUp(self):
        # Mock of Review Query
        review_json = open('../../data/book.json')
        # review_json = open('test/data/book.json')
        self.books_from_json = json.load(review_json)
        books_object_list = []
        self.books = ManageBooks()
        for book in self.books_from_json:
            books_object_list.append(Book(book))

    def test_create_new_book(self):
        """
            Expect to return flash_message when new book is created
        """
        self.books.create = MagicMock(return_value=None)
        create_book = self.books.create_one(self.books_from_json[0])
        self.assertEqual("Mock Book added!", create_book['flash_message'])

    def test_create_new_book_create_fails(self):
        """
            Expect to return flash_message with error if create response is not None
        """
        self.books.create = MagicMock(return_value="Error")
        create_review = self.books.create_one(self.books_from_json[0])
        self.assertEqual("Could Not Add book, Try Again", create_review['flash_message'])
