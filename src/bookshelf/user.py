from bson import ObjectId
from werkzeug.security import check_password_hash, generate_password_hash


class User:

    def __init__(self, user_info: dict):
        if user_info:
            self.__id = ObjectId(user_info.get('_id'))
            self.__username = user_info.get('username')
            self.__first_name = user_info.get('first')
            self.__last_name = user_info.get('last')
            self.__password = user_info.get('password')
            self.__moderator = user_info.get('moderator')
            self.__favorite_books = user_info.get('favorite_books')

    def get_id(self):
        return self.__id

    def get_first_name(self):
        if self.__first_name:
            return self.__first_name.capitalize()
        else:
            return self.__username

    def __set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        if self.__last_name:
            return self.__last_name.capitalize()

    def __set_last_name(self, last_name):
        self.__last_name = last_name

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

    def __set_password(self, new_password):
        self.__password = self.hash_password(new_password)

    def check_password(self, password_given: str):
        return check_password_hash(self.__password, password_given)

    def hash_password(self, password):
        return generate_password_hash(password)

    def get_dict(self):
        return {
            "username": self.get_username(),
            "first": self.get_first_name(),
            "last": self.get_last_name(),
            "password": self.hash_password(self.__password),
            "moderator": self.is_moderator(),
            "favorite_books": self.get_favorite_books()
        }

    def update_details(self, user_details: dict):
        """
        Updates user information from input dict
        :param user_details: {first_name, last_name, password, repeat_password}
        :return: None
        """

        for key, value in user_details.items():
            if key == 'first_name' and value != self.get_first_name():
                self.__set_first_name(value)
            if key == 'last_name' and value != self.get_last_name():
                self.__set_last_name(value)
            if key == 'password':
                # TODO Raise exception in case passwords don't match
                if value == user_details['repeat_password']:
                    self.__set_password(value)
