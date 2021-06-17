from werkzeug.security import check_password_hash, generate_password_hash


class User:

    def __init__(self, user_info: dict):
        if user_info:
            self.__id = user_info.get('_id')
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

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        if self.__last_name:
            return self.__last_name.capitalize()

    def set_last_name(self, last_name):
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

    def update_user_password(self, new_password: str):
        if new_password:
            self.__password = generate_password_hash(self.__password)

    def hash_password(self):
        if self.__password:
            self.__password = generate_password_hash(self.__password)

    def check_password(self, password_given: str):
        return check_password_hash(self.__password, password_given)

    def add_to_favorite_books(self, book_id: str):
        self.__favorite_books.append(book_id)

    def remove_from_favorites(self, book_id: str):
        self.__favorite_books.remove(book_id)

    def get_dict(self):
        return {
            "username": self.get_username(),
            "first": self.get_first_name(),
            "last": self.get_last_name(),
            "password": self.__password,
            "moderator": self.is_moderator(),
            "favorite_books": self.get_favorite_books()
        }
