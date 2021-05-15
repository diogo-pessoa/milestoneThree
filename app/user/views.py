from flask import Blueprint, render_template

from app.auth.views import login_required
from app.model.book_model import BookModel
from app.model.review_model import ReviewModel
from app.model.user_model import UserModel

user = Blueprint('user', __name__, template_folder='templates')


@user.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):

    logged_user = UserModel().find_user_by_name(username)
    reviews = ReviewModel().find_user_reviews(logged_user.get_id())
    user_favorite_books = logged_user.get_favorite_books()
    books = BookModel().find_books_by_id(user_favorite_books)
    # TODO Favorite_books.html missing book_rate
    return render_template("profile.html", user=logged_user, reviews=reviews, books=books)
