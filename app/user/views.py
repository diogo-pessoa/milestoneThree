from flask import Blueprint, render_template

from app.model.review_model import ReviewModel
from app.model.user_model import UserModel
from src.bookshelf.user import User

user = Blueprint('user', __name__, template_folder='templates')


@user.route("/profile/<user>", methods=["GET", "POST"])
def profile(user):
    user_information = UserModel().find_user_by_name(user)
    loaded_user = User(user_information)
    reviews = ReviewModel().find_all_user_reviews(loaded_user.get_username())
    return render_template("profile.html", user=loaded_user, reviews=reviews)
