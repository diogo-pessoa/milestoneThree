from bson import ObjectId

from app.model.bookshelf_model import BookshelfModel
from src.bookshelf.user import User


class ManageUsersSuper(object):
    """
        Super Class wrapping DataStorage calls for user documents
    """

    def __init__(self):
        self.model = BookshelfModel('users')

    def get_user(self, username: str):
        """
            queries data storage and return User() instance
            :param: username: str
            :return: User() Object with data from data storage
        """
        user = self.model.find_by_field_name_and_value(username, 'username')
        if user:
            return User(user)

    def get_by_id(self, user_id: str):
        """
        Get user Instance by Id
        :param user_id:
        :return: single User Instance
        """
        user = self.model.find_by_id(ObjectId(user_id))
        if user:
            return User(user)

    def create_user(self, new_user: User):
        """
            Proxy method call for create operation for dataStorage class.
            That simplifies the abstraction. single place to change if the model driver (Mongo,SQL) changes.
            :param new_user:
            :param username: User()
            :return: None or Error String
        """
        return self.model.create_one(new_user.get_dict())

    def update_user_information(self, update_information: User):
        """
            Proxy method call for create operation for dataStorage class.
            That simplifies the abstraction. single place to change if the model driver (Mongo,SQL) changes.
            :param update_information: User()
            :return: None or Error String
        """
        return self.model.update(update_information.get_id(), update_information.get_dict())


class ManageUsers(ManageUsersSuper):
    """
        Manages Bookshelf users operations and handling of user information updates
    """

    def __init__(self):
        super().__init__()

    def register(self, username: str, password: str, repeat_password: str):
        """
            Register new user if user is new and passwords match
        :param username:
        :param password:
        :param repeat_password:
        :return:
        """
        response = {
            "flash_message": "Invalid Credentials"
        }

        new_user = User({
            "username": username,
            "password": password,
        })
        # Check if User exists
        is_existing_user = self.get_user(new_user.get_username())

        if is_existing_user and is_existing_user.get_username() == username:
            response["flash_message"] = "username already in use"

        elif password == repeat_password:
            # hashing user password before storing in DB
            new_user.hash_password()
            create = self.create_user(new_user)  # returns None if create works
            if create:
                response["flash_message"] = "There was a problem when trying to create this user, Try Again!"
            else:
                response["flash_message"] = "Registration Successful!"
        else:
            response["flash_message"] = "Passwords do not match"

        return response["flash_message"]

    def login(self, username: str, password: str):
        """

        :return: dict with session and flash_message
        """
        response = {
            "session": None,
            "flash_message": "Invalid Credentials"
        }

        existing_user = self.get_user(username)
        if existing_user:

            if existing_user.check_password(password):
                response['session'] = existing_user.get_username()
                response['flash_message'] = "Welcome, {}".format(existing_user.get_first_name())
        return response

    def update_details(self, logged_user, new_information):
        """
        Updates user information from new_information dict
        :param logged_user: current user Object
        :param new_information: {first_name, last_name, password, repeat_password}
        :return: flash_message
        """
        response = {"flash_message": ""}
        for key, value in new_information.items():
            if key == 'first_name' and value != logged_user.get_first_name():
                logged_user.set_first_name(value)
            if key == 'last_name' and value != logged_user.get_last_name():
                logged_user.set_last_name(value)
            if key == 'password':
                if value == new_information['repeat_password']:
                    logged_user.update_user_password(value)
                else:
                    response["flash_message"] = "Password do not match, couldn't update information"
                    return response
        return_status = self.update_user_information(logged_user)
        if return_status:
            response["flash_message"] = "Something went wrong whe trying to update information, Try Again."
        else:
            response["flash_message"] = "Information Updated successfully"
        return response

    def add_to_favorite_books(self, book_id: str, logged_user: str):
        """

        :param book_id: str
        :param logged_user: str
        :return: None
        """
        user = self.get_user(logged_user)
        favorites_list = user.get_favorite_books()
        if book_id not in favorites_list:
            user.add_to_favorite_books(book_id)
            self.update_user_information(user)
            return f'Added to your Favorites list.'
        else:
            return f'Already in your favorites'
