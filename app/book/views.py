from flask import Blueprint, render_template, request

from app.auth.views import login_required
from app.model.book_model import BookModel
from app.model.review_model import ReviewModel

book = Blueprint('book', __name__, template_folder='templates')

review_model = ReviewModel()
book_model = BookModel()


@book.route('/book')
def book_list():
    books_list = book_model.find_all()
    return render_template('books.html', books=books_list)


@book.route("/book/<book_title>", methods=["GET"])
def book_page(book_title):
    single_book = book_model.find_by_title(book_title)
    book_rate = review_model.get_book_rate_by_title(single_book.get_title())
    reviews_for_book = review_model.find_all_book_reviews(single_book.get_title())
    return render_template('book.html', book=single_book, reviews=reviews_for_book, book_rate=book_rate)


@book.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books_list = book_model.search(query)
    return render_template("books.html", books=books_list)


@book.route("/book/edit/<book_id>", methods=["GET", "POST"])
@login_required
def edit(book_id):
    print(book_id)
    book_information = book_model.find_by_id(book_id)
    print(book_information)
    if request.method == "POST":
        pass
    return render_template("edit.html", book=book_information)
