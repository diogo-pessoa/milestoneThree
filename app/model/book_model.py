from bson import ObjectId

from app import mongo
from src.bookshelf.book import Book


class BookModel(object):

    def find_all(self):
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
            print(f"ERROR - Failed get all books from DB, {errno}: {strerror}.")

    def find_by_title(self, book_title: str):
        """
        Find book by title
        :param book_title: single book_name
        :return: Book object
        """

        try:
            single_book = mongo.db.books.find_one({"title": book_title.lower()})
            if single_book:
                return Book(single_book)
        except IOError as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to find book by title, {errno}: {strerror}.")

    def search(self, query):
        """
            Queries Mongo Collection search Index for Book Title or Author
        :param query:
        :return: List of Book Objects matching query search or None
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
            print(f"ERROR - Search Failed, {errno}: {strerror}.")

    def find_by_id(self, book_id):
        """
            Queries Mongo Collection search Index for Book Title or Author
        :param book_id:
        :return:  Book Object
        """
        try:
            book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
            if book:
                return Book(book)
        except IOError as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to find book by id, {errno}: {strerror}.")

    def find_list_by_id(self, user_favorite_book_ids: list):
        """
        Takes a list of book_Ids query each appending result to return list
        :return: Returns list of Book Objects
        """
        try:
            books = []
            for book_id in user_favorite_book_ids:
                books.append(self.find_by_id(book_id))
            return books
        except Exception as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to update book, {errno}: {strerror}.")

    def update_book(self, book_id, book_information):
        """
         Push Update book Information to Mongo
         Returns book_title_for_url as update can change book title, and we are using book title as part of book url
        :return: title_for_url in case there's a change.
        """
        try:
            new_book_details = Book(book_information)
            mongo.db.books.update({"_id": ObjectId(book_id)}, new_book_details.get_dict())
            return new_book_details.get_raw_title()
        except Exception as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to update book, {errno}: {strerror}.")


    def create_one(self, new_book_information):
        """
         Create new book from book Object
         Returns book_title for url, in order to allow for page redirect
        :return: title_for_url
        """
        try:
            #TODO check if book already exists.
            # return link if it does
            new_book_details = Book(new_book_information)
            book = mongo.db.books.insert(new_book_details.get_dict())
            print(book)
            return new_book_details
        except Exception as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to update book, {errno}: {strerror}.")