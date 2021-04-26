from flask import Flask
from flask_pymongo import PyMongo

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

from app.auth.views import auth
from app.main.views import main
from app.user.views import user

app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(user)
