from flask import Blueprint, render_template

from app.model.book_model import BookModel

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
@main.route('/index')
def index():
    books = BookModel().find_all_books()
    return render_template('index.html', books=books)
