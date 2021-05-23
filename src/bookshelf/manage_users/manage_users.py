from app.model.user_model import UserModel
from src.bookshelf.user import User


class ManageUsers:

    def register(self, user_information: dict):
        """

        :param user_information:
        :return: response ( User(), Flash message)
        """
        repeat_password = user_information.get("repeat_password")
        # Instance of User
        new_user = User({
            "username": user_information.get("username"),
            "password": user_information.get("password"),
        })
        # Check if User exists
        user = UserModel().find_user_by_name(new_user.get_username())

        if user:
            register_message = "username already in use"
        elif not new_user.check_password(repeat_password):
            register_message = "Passwords do not match"
        else:
            # create user
            create_user = UserModel().create(new_user)
            if create_user == None:
                register_message = "Registration Successful!"
            else:
                register_message = "There was a problem when trying to create this user, Try Again!"
        return register_message
