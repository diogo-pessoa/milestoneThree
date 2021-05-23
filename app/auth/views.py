from functools import wraps

from flask import Blueprint, request, flash, redirect, url_for, render_template, session

from src.bookshelf.manage_users.manage_users import ManageUsers

auth = Blueprint('auth', __name__, template_folder='templates')

manage_users = ManageUsers()


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        register_message = manage_users.register(request.form.get("username"), request.form.get("password"),
                                                 request.form.get("repeat_password"))
        flash(register_message)
    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_login = manage_users.login(request.form.get("username"), request.form.get("password"))
        flash(user_login["flash_message"])
        if user_login.get('session'):
            session["user"] = user_login.get('session')
            return redirect(url_for("book.book_list"))
        else:
            return redirect(url_for("auth.login"))
    return render_template("login.html")


@auth.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("book.book_list"))


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session:
            flash("Login to execute this operation")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)

    return decorated_function
