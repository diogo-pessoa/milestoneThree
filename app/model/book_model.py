from app import mongo
from src.bookshelf.book import Book


class BookModel(object):

    def find_all_books(self):
        """
        Returns a list with all Books from Books collections
        :return: list of Book objects from DB
        """
        books = []
        books_from_db = mongo.db.books.find()
        for book in books_from_db:
            books.append(Book(book))
        return books
