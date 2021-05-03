from flask import Blueprint, render_template

from app.model.book_model import BookModel
from app.model.review_model import ReviewModel

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
@main.route('/index')
def index():
    books = BookModel().find_all_books()
    reviews = ReviewModel().find_all_user_reviews("willfarnaby")
    return render_template('index.html', books=books, reviews=reviews)
