from werkzeug.security import generate_password_hash

from app import mongo


class User(object):

    def __init__(self, **user_info):
        if user_info:
            self.username = user_info['username']
            self.username = user_info['password']
            self.username = user_info['is_moderator']
            self.username = user_info['favorite_books']

    def find_user_by_name(self, name: str):
        try:
            user = mongo.db.users.find_one({"username": name.lower()})
            if user:
                return user.get("username")

        except IOError as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to get user, {errno}: {strerror}.")

    def insert_new_user(self, username: str, password: str):
        user_details = {
            "username": username.lower(),
            "password": generate_password_hash(password),
            "is_moderator": False,
            "favorite_books": []
        }
        try:
            mongo.db.users.insert_one(user_details)
        except Exception as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to Insert user:, {errno}: {strerror}.")