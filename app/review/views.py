from flask import Blueprint, render_template, request, url_for, session
from werkzeug.utils import redirect

from src.bookshelf.manage_books.manage_books import ManageBooks
from src.bookshelf.manage_reviews.manage_reviews import ManageReviews
from src.bookshelf.manage_users.manage_users import ManageUsers

review = Blueprint('review', __name__, template_folder='templates')
books = ManageBooks()
reviews = ManageReviews()
users = ManageUsers()


@review.route('/add_review/<book_title>', methods=["GET", "POST"])
def add(book_title):
    book = books.get_by_title(book_title)
    if request.method == "POST":
        user_id = users.get_user(session['user']).get_id()
        reviews.add_new_review(book.get_id(), user_id, request.form.get("book_rate"),
                               request.form.get("book_review"))
        return redirect(url_for('book.book_page', book_title=book_title))
    return render_template('add_review.html', book=book)
