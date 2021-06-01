from flask import Blueprint, render_template, url_for, flash, request
from werkzeug.utils import redirect

from app.auth.views import login_required
from app.model.book_model import BookModel
from src.bookshelf.manage_reviews.manage_reviews import ManageReviews
from src.bookshelf.manage_users.manage_users import ManageUsers

user = Blueprint('user', __name__, template_folder='templates')

manage_users = ManageUsers()
manage_reviews = ManageReviews()


@user.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    logged_user = manage_users.get_user(username)
    if request.method == "POST":
        update = manage_users.update_details(logged_user, request.form)
        flash(update["flash_message"])
        return redirect(url_for('user.profile', username=logged_user.get_username()))
    reviews = manage_reviews.get_reviews(logged_user.get_id(), 'reviewer_id')
    user_favorite_books = logged_user.get_favorite_books()
    books = BookModel().find_list_by_id(user_favorite_books)
    # TODO Favorite_books.html missing book_rate
    return render_template("profile.html", user=logged_user, reviews=reviews, books=books)
