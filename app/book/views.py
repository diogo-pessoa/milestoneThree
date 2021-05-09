from flask import Blueprint, render_template, request

from app.model.book_model import BookModel
from app.model.review_model import ReviewModel

book = Blueprint('book', __name__, template_folder='templates')

review_model = ReviewModel()
book_model = BookModel()


@book.route('/book')
def book_list():
    books_list = book_model.find_all_books()
    return render_template('books.html', books=books_list)


@book.route("/book/<book_name>", methods=["GET"])
def book_page(book_name):
    single_book = book_model.find_book_by_title(book_name)
    book_rate = review_model.get_book_rate_by_title(single_book.get_title())
    reviews_for_book = review_model.find_all_book_reviews(single_book.get_title())
    return render_template('book.html', book=single_book, reviews=reviews_for_book, book_rate=book_rate)


@book.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books_list = book_model.search_for_book(query)
    return render_template("books.html", books=books_list)
