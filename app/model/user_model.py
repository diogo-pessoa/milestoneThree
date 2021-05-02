from app import mongo

class UserModel(object):

    def find_user_by_name(self, name: str):
        """
            Queries Mongo users collection filtering by username
        :param name:
        :return: dict with user information or empty dict
        """
        try:
            user = mongo.db.users.find_one({"username": name.lower()})
            if user:
                return user

        except IOError as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to get user, {errno}: {strerror}.")

    def save(self, user_data):
        """
        Create New object in users collection
        :param user_data: User info on first login only user & password
        :return: None
        """
        try:

            mongo.db.users.insert_one(user_data)
        except Exception as e:
            errno, strerror = e.args
            print(f"ERROR - Failed to Insert user:, {errno}: {strerror}.")
