from flask import Blueprint, render_template, url_for, flash, request, session
from werkzeug.utils import redirect

from app.auth.views import login_required
from src.bookshelf.manage_books.manage_books import ManageBooks
from src.bookshelf.manage_reviews.manage_reviews import ManageReviews
from src.bookshelf.manage_users.manage_users import ManageUsers

user = Blueprint('user', __name__, template_folder='templates')

users = ManageUsers()
reviews = ManageReviews()
books = ManageBooks()


@user.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    logged_user = users.get_user(username)
    if request.method == "POST":
        user_update = users.update_details(logged_user, request.form)
        flash(user_update["flash_message"])
        return redirect(url_for('user.profile', username=logged_user.get_username()))
    user_favorite_books = logged_user.get_favorite_books()
    book_list = books.get_many_by_id(user_favorite_books)
    return render_template("profile.html", user=logged_user,
                           reviews=reviews.get_many(logged_user.get_id(), 'reviewer_id'),
                           books=book_list)


@user.route("/add_to_favorites/<book_id>", methods=["POST"])
@login_required
def add_to_favorites(book_id):
    if request.method == "POST":
        logged_user = session['user']
        book = books.get_one_by_id(book_id)
        favorite_message = users.add_to_favorite_books(book_id, logged_user)
        flash(favorite_message)
        return redirect(url_for('book.book_page', book_title=book.get_title_for_url()))