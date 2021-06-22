from flask import Blueprint, render_template, request, flash, url_for, session
from werkzeug.utils import redirect

from app.auth.views import login_required
from src.bookshelf.manage_books.manage_books import ManageBooks
from src.bookshelf.manage_reviews.manage_reviews import ManageReviews
from src.bookshelf.manage_users.manage_users import ManageUsers

book = Blueprint('book', __name__, template_folder='templates')

reviews = ManageReviews()
books = ManageBooks()
users = ManageUsers()


@book.route('/book')
def book_list():
    return render_template('books.html', books=books.get_all())


@book.route("/book/<book_title>", methods=["GET"])
def book_page(book_title):
    book_in_page = books.get_by_title(book_title)
    book_rate = reviews.get_rate_by_book_id(book_in_page.get_id())
    reviews_for_book = reviews.get_reviews(book_in_page.get_id(), 'book_id')
    logged_user = None
    if 'user' in session:
        logged_user = users.get_user(session['user'])

    return render_template('book.html', book=book_in_page, reviews=reviews_for_book, book_rate=book_rate,
                           logged_user=logged_user)


@book.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books_list = books.search(query)
    return render_template("books.html", books=books_list)


@book.route("/book/edit/<book_id>", methods=["GET", "POST"])
@login_required
def edit(book_id):
    book_information = books.get_one_by_id(book_id)

    if request.method == "POST":
        book_edit_form = request.form
        update_response = books.update_details(book_id, book_edit_form)
        flash(update_response["flash_message"])
        return redirect(url_for('book.book_page', book_title=update_response['book_url_title']))
    return render_template("edit.html", book=book_information)


@book.route("/book/new/", methods=["GET", "POST"])
@login_required
def new():
    if request.method == "POST":
        new_book_information = request.form
        create_response = books.create_one(new_book_information)
        flash(create_response['flash_message'])
        return redirect(url_for('book.book_page', book_title=create_response['book_url_title']))
    return render_template("new.html")


@book.route("/book/delete/<book_id>", methods=["POST"])
@login_required
def delete(book_id):
    if request.method == "POST":
        books.delete(book_id)
        flash('Book Removed')
        return redirect(url_for('book.book_list'))
