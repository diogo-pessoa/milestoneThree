from flask import Blueprint, render_template, request, flash, url_for
from werkzeug.utils import redirect

from app.auth.views import login_required
from app.model.book_model import BookModel
from app.model.review_model import ReviewModel
from app.model.user_model import UserModel

book = Blueprint('book', __name__, template_folder='templates')

review_model = ReviewModel()
book_model = BookModel()

@book.route('/book')
def book_list():
    books_list = book_model.find_all()
    return render_template('books.html', books=books_list)


@book.route("/book/<book_title>", methods=["GET"])
def book_page(book_title):
    book = book_model.find_by_title(book_title)
    book_rate = review_model.get_rate_by_book_id(book.get_id())
    reviews_for_book = review_model.get_by_book_id(book.get_id())
    return render_template('book.html', book=book, reviews=reviews_for_book, book_rate=book_rate)


@book.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books_list = book_model.search(query)
    return render_template("books.html", books=books_list)


@book.route("/book/edit/<book_id>", methods=["GET", "POST"])
@login_required
def edit(book_id):
    book_information = book_model.find_by_id(book_id)

    if request.method == "POST":
        book_edit_form = request.form
        new_book_information = book_model.update_book(book_id, book_edit_form)
        flash("Book Information Updated")
        return redirect(url_for('book.book_page', book_title=new_book_information))
    return render_template("edit.html", book=book_information)
