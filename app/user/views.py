from flask import Blueprint, render_template

user = Blueprint('user', __name__, template_folder='templates')


@user.route("/profile/<user>", methods=["GET", "POST"])
def profile(user):
    #
    return render_template("profile.html", user=str(user).capitalize())
