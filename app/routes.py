from flask import (render_template, request,
                   flash, redirect, url_for)

from app import app
from app.model.book_model import Book
from app.model.review_model import Review
from app.model.user_model import User


@app.route('/')
@app.route('/index')
def index():
    books = Book().find_all_books()
    reviews = Review().find_all_reviews()
    user = User().find_user_by_name("Name")
    return render_template('index.html', books=books, reviews=reviews, user=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        existing_user = User().find_user_by_name(username)
        if existing_user:
            flash("username already in use")
            return redirect(url_for("register"))

        # Insert new user
        User().insert_new_user(username,
                               password)
        flash("Registration Successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")
