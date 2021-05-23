from flask import Flask
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

app.register_blueprint(auth)
app.register_blueprint(review)
app.register_blueprint(user)
app.register_blueprint(book)
