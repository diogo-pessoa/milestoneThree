from flask import render_template
from app import app
from app.models import Data


@app.route('/')
@app.route('/index')
def index():
    books = Data().find_all_books()
    reviews = Data().find_all_books()
    user = Data().find_user_by_name("Name")
    return render_template('index.html', books=books, reviews=reviews, user=user)
