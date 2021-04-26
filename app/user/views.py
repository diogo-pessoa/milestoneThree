from flask import Blueprint, render_template, session

user = Blueprint('user', __name__, template_folder='templates')


@user.route("/profile/<user>", methods=["GET", "POST"])
def profile(user):
    # grab user session from local cookie.
    user = session["user"]
    return render_template("profile.html", user=user)




