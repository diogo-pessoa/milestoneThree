from flask import Blueprint, render_template

from app.model.review_model import ReviewModel
from app.model.user_model import UserModel

user = Blueprint('user', __name__, template_folder='templates')


@user.route("/profile/<user>", methods=["GET", "POST"])
def profile(user):
    logged_user = UserModel().find_user_by_name(user)
    reviews = ReviewModel().find_all_user_reviews(logged_user.get_username())
    return render_template("profile.html", user=logged_user, reviews=reviews)
