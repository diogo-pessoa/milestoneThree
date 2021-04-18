from werkzeug.security import generate_password_hash

from app import mongo


class Data(object):
    # TODO insert try
    def find_all_books(self):
        return mongo.db.books.find()

    def find_all_reviews(self):
        reviews = mongo.db.reviews.find()
        return reviews

    def find_user_by_name(self, name: str):
        try:
            user = mongo.db.users.find_one({"username": name.lower()})
            if user:
                return user.get("username")

        except IOError as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to get user, {errno}: {strerror}.")

    def insert_new_user(self, username, password):
        user_details = {
            "username": username.lower(),
            "password": generate_password_hash(password)
        }
        try:
            mongo.db.users.insert_one(user_details)
        except Exception as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to Insert user:, {errno}: {strerror}.")
