from flask import Flask, render_template
from flask_pymongo import PyMongo

from config import Config


def get_app_with_config(config):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config)
    py_mongo = PyMongo(flask_app)
    return flask_app, py_mongo


app, mongo = get_app_with_config(Config)

from app.auth.views import auth
from app.review.views import review
from app.user.views import user
from app.book.views import book
from app.landing.views import landing

app.register_blueprint(auth)
app.register_blueprint(review)
app.register_blueprint(user)
app.register_blueprint(book)
app.register_blueprint(landing)


@app.errorhandler(404)
def page_not_found(e):
    error_message = "Page Not Found"
    return render_template('error_page.html', message=error_message), 404


@app.errorhandler(500)
def page_not_found(e):
    error_message = "This was not supposed to happen"
    return render_template('error_page.html', message=error_message), 500
