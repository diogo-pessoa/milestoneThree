from werkzeug.security import generate_password_hash


class User:

    def __init__(self, user_info: dict):
        if user_info:
            self.username = user_info.get('username')
            self.first_name = user_info.get('first')
            self.last_name = user_info.get('last')
            self.password = generate_password_hash(user_info.get('password'))
            self.moderator = user_info.get('moderator')
            self.favorite_books = user_info.get('favorite_books')

    def get_first_name(self):
        if self.first_name:
            return self.first_name.capitalize()

    def get_last_name(self):
        if self.last_name:
            return self.last_name.capitalize()

    def get_username(self):
        if self.username:
            return self.username

    def get_favorite_books(self):
        if self.favorite_books:
            return self.favorite_books
        else:
            return []

    def is_moderator(self):
        if self.moderator == 1:
            return True
        return False

    def get_instance(self):
        return {
            "username": self.username,
            "first": self.first_name,
            "last": self.last_name,
            "password": self.password,
            "moderator": self.moderator,
            "favorite_books": self.favorite_books
        }
