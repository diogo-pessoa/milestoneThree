from bson import ObjectId

from app.model.bookshelf_model import BookshelfModel
from src.bookshelf.book import Book


class ManageBooksSuper(object):
    """
        Super Class wrapping DataStorage calls for Book documents
    """

    def __init__(self):
        self.model = BookshelfModel('books')

    def create(self, book: Book):
        """
            Wrapper method for Model
            :param book: Book
            :return: None
        """
        create_book = self.model.create_one(book.get_dict())
        if not create_book:
            return create_book

    def update(self, book_id: ObjectId, book: dict):
        """
            Wrapper method for Model to update a book document
            :param book_id: ObjectId
            :param book: Book
            :return: None
        """
        update = self.model.update(book_id, book)
        if not update:
            return update

    def delete(self, book_id: ObjectId):
        """
            Wraps Model delete call
            :param book_id: ObjectId
            :return: None
        """
        delete = self.model.delete_by_id(ObjectId(book_id))
        if not delete:
            return delete

    def get_by_title(self, value: str):
        """
            Queries Data Storage for Book based on attribute_name
            :param object_id: str
            :return: book: Book
        """
        book = Book(self.model.find_by_field_name_and_value(value, 'title'))
        if book:
            return book

    def search(self, query: str):
        """
            Wrap search call for Collection search Index for Book Title or Author (Based Mongo Search Index)
            :param query: str
            :return: list of books matching search query
        """
        query_results = []
        search_books_query_result = self.model.search(query)
        if search_books_query_result:
            for book in search_books_query_result:
                query_results.append(Book(book))
            return query_results

    def get_one_by_id(self, object_id: str):
        """
            Queries Data Storage for Book based on attribute_name
            :param object_id: object_id
            :return: book: Book
        """
        book = Book(self.model.find_by_id(ObjectId(object_id)))
        if book:
            return book

    def get_all(self):
        response = []
        books = self.model.find_all()
        for book in books:
            response.append(Book(book))
        return response


class ManageBooks(ManageBooksSuper):

    def __init__(self):
        super().__init__()

    def create_one(self, new_book_details: dict):
        """
        Adds new Book from dict with information passed from web form
        :param new_book_details:
        :return:
        """
        # TODO check for existing book
        response = {
            "flash_message": "",
            "book_url_title": ""
        }
        book = Book(new_book_details)
        create_book = self.create(book)
        if create_book is not None:
            response['flash_message'] = "Could Not Add book, Try Again"
        else:
            response['flash_message'] = f'{book.get_formatted_title()} added!'
            response['book_url_title'] = book.get_title_for_url()
        return response

    def update_details(self, book_id: str, new_book_details: dict):
        """
        Push Update book Information to Mongo
        :param book_id:
        :param new_book_details:
        :return: response: dict {flash_message, book_title}
        """
        response = {
            "flash_message": "",
            "book_title": ""
        }
        book = Book(new_book_details)

        # TODO Get Book by id needed for update
        book = Book(new_book_details)
        create_book = self.update(ObjectId(book_id), book.get_dict())
        if create_book is not None:
            response['flash_message'] = "Could Not Add book, Try Again"
        else:
            response['flash_message'] = f'{book.get_formatted_title()} added!'
            response['book_url_title'] = book.get_title_for_url()
        return response

    def delete_book_by_id(self, book_id: str):
        """
        Checks reviewer_id matches user_id then request object deletion
        :param book_id: str
        :return: response: dict
        """
        response = {
            'flash_message': "Book deleted successfully."
        }
        delete_book = self.delete(ObjectId(book_id))
        if delete_book is not None:
            response['flash_message'] = "Could Not delete book, Try Again"
        return response

    def get_many_by_id(self, ids: list):
        books = []
        book = None
        for book_id in ids:
            book = self.get_one_by_id(book_id)
            books.append(book)
        if book:
            return books
