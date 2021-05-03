from werkzeug.security import check_password_hash, generate_password_hash


class User:

    def __init__(self, user_info: dict):
        if user_info:
            self.__username = user_info.get('username')
            self.__first_name = user_info.get('first')
            self.__last_name = user_info.get('last')
            self.__password = user_info.get('password')
            self.__moderator = user_info.get('moderator')
            self.__favorite_books = user_info.get('favorite_books')

    def get_first_name(self):
        if self.__first_name:
            return self.__first_name.capitalize()
        else:
            return self.__username

    def get_last_name(self):
        if self.__last_name:
            return self.__last_name.capitalize()

    def get_username(self):
        if self.__username:
            return self.__username.lower()

    def get_favorite_books(self):
        if self.__favorite_books:
            return self.__favorite_books
        else:
            return []

    def is_moderator(self):
        if self.__moderator == 1:
            return True
        return False

    def check_password(self, password_given: str):
        return check_password_hash(self.__password, password_given)

    def hash_password(self):
        return generate_password_hash(self.__password)

    def get_dict(self):
        return {
            "username": self.get_username(),
            "first": self.get_first_name(),
            "last": self.get_last_name(),
            "password": self.hash_password(),
            "moderator": self.is_moderator(),
            "favorite_books": self.get_favorite_books()
        }
