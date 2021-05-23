from app.model.user_model import UserModel
from src.bookshelf.user import User


class ManageUsers:

    def register(self, user_information: dict):
        """

        :param user_information:
        :return: dict with flash_message
        """
        repeat_password = user_information.get("repeat_password")
        # Instance of User
        new_user = User({
            "username": user_information.get("username"),
            "password": user_information.get("password"),
        })
        # Check if User exists
        is_existing_user = UserModel().find_user_by_name(new_user.get_username())
        new_user.hash_user_password()
        if is_existing_user:
            register_message = "username already in use"
        elif not new_user.check_password(repeat_password):
            register_message = "Passwords do not match"
        else:
            # create user
            create_user = UserModel().create(new_user)
            # TODO make it clearer create User worked and default return is None
            if not create_user:
                register_message = "Registration Successful!"
            else:
                register_message = "There was a problem when trying to create this user, Try Again!"
        return register_message

    def login(self, username: str, password: str):
        """

        :return: dict with session and flash_message
        """
        response = {
            "session": None,
            "flash_message": "Invalid Credentials"
        }

        existing_user = UserModel().find_user_by_name(username)
        if existing_user:
            user = User(existing_user)
            if user.check_password(password):
                response['session'] = user.get_username()
                response['flash_message'] = "Welcome, {}".format(user.get_first_name())
        return response
