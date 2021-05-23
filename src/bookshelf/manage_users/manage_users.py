from app.model.user_model import UserModel
from src.bookshelf.user import User


class ManageUsers:

    def get_user(self, username):
        user = UserModel().find_user_by_name(username)
        if user:
            return User(user)

    def create_user(self, new_user: User):
        return UserModel().create(new_user)

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
