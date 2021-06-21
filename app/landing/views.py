from flask import Blueprint, render_template, session, url_for
from werkzeug.utils import redirect

landing = Blueprint('landing', __name__, template_folder='templates')


@landing.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('book.book_list'))
    return render_template('index.html')
