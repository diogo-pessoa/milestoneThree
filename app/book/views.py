from flask import Blueprint, render_template

from app.model.book_model import BookModel

book = Blueprint('book', __name__, template_folder='templates')


@book.route('/book')
def book_list():
    books_list = BookModel().find_all_books()
    return render_template('books.html', books=books_list)


@book.route("/book/<book_name>", methods=["GET", "POST"])
def book_page(book_name):
    single_book = BookModel().find_book_by_title(book_name)
    return render_template('book.html', book=single_book)
