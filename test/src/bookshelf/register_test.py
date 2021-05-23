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

    def test_register_with_passwords_not_matching(self):
        """
        Tries to register new user with passwords that do not match

        """
        register = self.manage_user.register("new_user", "12345", "1234")
        self.assertEqual("Passwords do not match", register)

    def test_register_with_existing_username(self):
        """
            Fail to register with existing User
        """

        register = self.manage_user.register("willfarnaby", "12345", "12345")
        self.assertEqual("username already in use", register)

    def test_register_new_user(self):
        """
            Fail to register with user already in DB
        """
        self.manage_user.get_user = MagicMock(return_value=None)
        self.manage_user.create_user = MagicMock(return_value=None)
        register = self.manage_user.register("new_user", "12345", "12345")
        self.assertEqual("Registration Successful!", register)

    def test_register_new_user_create_returns_Error(self):
        """
            Fail to register with user already in DB
        """
        self.manage_user.get_user = MagicMock(return_value=None)
        self.manage_user.create_user = MagicMock(return_value="Error")
        register = self.manage_user.register("new_user", "12345", "12345")
        self.assertEqual("There was a problem when trying to create this user, Try Again!", register)
