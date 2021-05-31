from app.model.user_model import UserModel
from src.bookshelf.user import User


class ManageUsers:
    """
        Manages Bookshelf users operations and handling of user information updates
    """

    def __init__(self):
        self.user_model = UserModel()

    def get_user(self, username: str):
        """
            queries data storage and return User() instance
            :param: username: str
            :return: User() Object with data from data storage
        """
        user = self.user_model.find_user_by_name(username)
        if user:
            return User(user)

    def create_user(self, new_user: User):
        """
            Proxy method call for create operation for dataStorage class.
            That simplifies the abstraction. single place to change if the model driver (Mongo,SQL) changes.
            :param username: User()
            :return: None or Error String
        """
        return self.user_model.create(new_user)

    def update_user_information(self, update_information: User):
        """
            Proxy method call for create operation for dataStorage class.
            That simplifies the abstraction. single place to change if the model driver (Mongo,SQL) changes.
            :param update_information: User()
            :return: None or Error String
        """
        return self.user_model.update(update_information)

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
