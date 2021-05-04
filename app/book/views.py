from flask import Blueprint, render_template

from app.model.book_model import BookModel

book = Blueprint('book', __name__, template_folder='templates')


@book.route('/')
@book.route('/books')
def book_list():
    books_list = BookModel().find_all_books()
    return render_template('books.html', books=books_list)


@book.route("/book/<book_name>", methods=["GET", "POST"])
def book_page(book_name):
    return render_template('book.html', book=book_name)
