from flask import Blueprint, request, flash, redirect, url_for, render_template

from app.model.user_model import User

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        existing_user = User().find_user_by_name(username)
        if existing_user:
            flash("username already in use")
            return redirect(url_for("auth.register"))

        # Insert new user
        User().insert_new_user(username,
                               password)
        flash("Registration Successful!")
    return render_template("register.html")


@auth.route("/login", methods=["GET"])
def login():
    return render_template("login.html")
