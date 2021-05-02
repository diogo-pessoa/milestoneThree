from flask import Blueprint, request, flash, redirect, url_for, render_template, session
from werkzeug.security import check_password_hash

from app.model.user_model import UserModel
from src.bookshelf.user import User

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User({"username": request.form.get("username"),
                     "password": request.form.get("password")
                     })
        is_new_user = UserModel().find_user_by_name(user.get_username())
        if is_new_user:
            flash("username already in use")
            return redirect(url_for("auth.register"))
        # Insert new user
        UserModel().save(user.get_instance())
        flash("Registration Successful!")
    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # check if username exists in db
        existing_user = UserModel().find_user_by_name(username)
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user.get("password"), password):
                session["user"] = username
                flash("Welcome, {}".format(username))
                return redirect(url_for("main.index"))
            else:
                # invalid password match
                flash("Invalid Credentials")
                return redirect(url_for("auth.login"))
        else:
            # username doesn't exist
            flash("Invalid Credentials")
            return redirect(url_for("auth.login"))
    return render_template("login.html")


@auth.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("main.index"))
