from bson import ObjectId

from app import mongo
from src.bookshelf.user import User


class UserModel(object):

    def find_user_by_name(self, name: str):
        """
            Queries Mongo users collection filtering by username
        :param name:
        :return: User() Object Instance of User Class
        """
        try:
            user = mongo.db.users.find_one({"username": name.lower()})
            if user:
                returned_user = User(user)
                return returned_user

        except IOError as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to get user, {errno}: {strerror}.")

    def find_by_id(self, user_id: ObjectId()):
        """
            Queries Mongo users collection filtering by _id
        :param user_id: ObjectId
        :return: Object Instance of User Class
        """
        try:
            user = mongo.db.users.find_one({"_id": user_id})
            if user:
                returned_user = User(user)
                return returned_user

        except IOError as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to get user, {errno}: {strerror}.")

    def create(self, username: str, password: str):
        """
        Create New object in users collection
        :param user_data: User info on first login only user & passwordw
        :return: None
        """
        try:
            user_data = User({"username": username,
                              "password": password
                              })
            mongo.db.users.insert_one(user_data.get_dict())
        except Exception as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to Insert user:, {errno}: {strerror}.")

    def update(self, user: User, user_information_form_content: dict):
        """
            Push Update book Information to Mongo
            Returns book_title_for_url as update can change book title, and we are using book title as part of book url
            :return: title_for_url in case there's a change.
        """
        try:
            user.update_details(user_information_form_content)
            mongo.db.users.update({"_id": user.get_id()}, user.get_dict())
        except Exception as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to update book, {errno}: {strerror}.")
