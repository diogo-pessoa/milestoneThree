from app import mongo
from src.bookshelf.book import Book


class BookModel(object):

    def find_all_books(self):
        """
        Returns a list with all Books from Books collections
        :return: list of Book objects from DB
        """
        try:
            books = []
            books_from_db = mongo.db.books.find()
            for book in books_from_db:
                books.append(Book(book))
            return books

        except IOError as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to get user, {errno}: {strerror}.")

    def find_book_by_title(self, book_name: str):
        """
        Find book by title
        :param book_name: single book_name
        :return: Book object
        """

        try:
            single_book = mongo.db.books.find_one({"title": book_name})
            if single_book:
                return Book(single_book)
        except IOError as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to get user, {errno}: {strerror}.")

    def search_for_book(self, query):
        """
            Queries Mongo Collection search Index for Book Title or Author
        :param query:
        :return: List of Book Objects matchint query search or None
        """
        query_results = []
        try:
            search_books_query = mongo.db.books.find({"$text": {"$search": query}})
            if search_books_query:
                for book in search_books_query:
                    query_results.append(Book(book))
                return query_results
        except IOError as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to get user, {errno}: {strerror}.")
