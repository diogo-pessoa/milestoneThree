from flask import (render_template, request,
                   flash, redirect, url_for, session)
from app import app
from app.models import Data


@app.route('/')
@app.route('/index')
def index():
    books = Data().find_all_books()
    reviews = Data().find_all_books()
    user = Data().find_user_by_name("Name")
    return render_template('index.html', books=books, reviews=reviews, user=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        existing_user = Data().find_user_by_name(username)
        if existing_user:
            flash("username already in use")
            return redirect(url_for("register"))

        # Insert new user
        Data().insert_new_user(username,
                               password)
        flash("Registration Successful!")
    return render_template("register.html")
