from functools import wraps

from flask import Blueprint, request, flash, redirect, url_for, render_template, session

from app.model.user_model import UserModel

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # TODO validate password

        new_user = UserModel().find_user_by_name(username)
        if new_user:
            flash("username already in use")
            return redirect(url_for("auth.register"))

        UserModel().create(username, password)
        flash("Registration Successful!")
    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form_details = {"username": request.form.get("username"),
                        "password": request.form.get("password")
                        }
        # check if username exists
        existing_user = UserModel().find_user_by_name(form_details['username'])
        if existing_user:
            # ensure hashed password matches user input
            if existing_user.check_password(form_details["password"]):
                session["user"] = existing_user.get_username()
                flash("Welcome, {}".format(existing_user.get_first_name()))
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


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session:
            flash("Login to execute this operation")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)

    return decorated_function
