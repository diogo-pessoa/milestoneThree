from flask import Blueprint, render_template

from app.model.book_model import Book
from app.model.review_model import Review
from app.model.user_model import User

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
@main.route('/index')
def index():
    books = Book().find_all_books()
    reviews = Review().find_all_reviews()
    return render_template('index.html', books=books, reviews=reviews)
