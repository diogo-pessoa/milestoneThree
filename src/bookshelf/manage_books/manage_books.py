from app.model.book_model import BookModel
from src.bookshelf.book import Book


class ManageBooksSuper(object):

    def __init__(self):
        self.model = BookModel()

    def create(self, book: Book):
        """
            Wrapper method for Book Model to insert new book
        :param book: Book
        :return: None
        """
        create_book = self.model.create_one(book.get_dict())
        if not create_book:
            return create_book

    def update(self, book: Book):
        """
            Wrapper method for Book Model to update new book
        :param book: Book
        :return: None
        """
        update = self.model.update(book.get_id(), book.get_dict())
        if not update:
            return update


class ManageBooks(ManageBooksSuper):

    def __init__(self):
        super().__init__()

    def create_one(self, new_book_details: dict):
        """
        Adds new Book from dict with information passed from web form
        :param new_book_details:
        :return:
        """
        response = {
            "flash_message": ""
        }

        book = Book(new_book_details)
        create_book = self.create(book)
        if create_book is not None:
            response['flash_message'] = "Could Not Add book, Try Again"
        else:
            response['flash_message'] = f'{book.get_formatted_title()} added!'
        return response

    def update_details(self, new_book_details: dict):
        """
                 Push Update book Information to Mongo
                 Returns book_title_for_url as update can change book title, and we are using book title as part of book url
                :return: title_for_url in case there's a change.
        """
        # try:
        #     new_book_details = Book(book_information)
        #     mongo.db.books.update({"_id": ObjectId(book_id)}, new_book_details.get_dict())
        #     return new_book_details.get_raw_title()
        # except Exception as e:
        #     errno, strerror = e.args
        #     print(f"ERROR - Failed to update book, {errno}: {strerror}.")
