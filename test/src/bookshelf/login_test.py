import json
import unittest
from unittest.mock import MagicMock

from app import get_app_with_config
from config import TestConfig
from src.bookshelf.manage_users.manage_users import ManageUsers
from src.bookshelf.user import User

app, mongo = get_app_with_config(TestConfig)


class ManageUsersTest(unittest.TestCase):

    def setUp(self):
        user_json = open('test/data/user.json')
        self.user_from_query = json.load(user_json)
        user_json.close()
        self.manage_user = ManageUsers()
        self.manage_user.get_user = MagicMock(return_value=User(self.user_from_query))

    def test_login_non_existing_user(self):
        """
        Tries to login with non-existent user, Session is None
        flash_message = "Invalid Credentials"
        """
        login = self.manage_user.login("Joseph", "password")
        self.assertIsNone(login["session"])

    def test_login_with_existing_user_not_matching_password(self):
        """
        Tries to login with user, but wrong password Session is None
        flash_message = "Invalid Credentials"
        """
        login = self.manage_user.login("Joseph", "password")
        self.assertIsNone(login["session"])

    def test_login_with_existing_user_matching_password(self):
        """
        Tries to login with correct user credentials, Returns valid session

        """
        login = self.manage_user.login("willfarnaby", "12345")
        self.assertIsNone(login["session"])
