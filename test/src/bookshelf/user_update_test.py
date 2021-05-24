import json
import unittest
from unittest.mock import MagicMock

from app import get_app_with_config
from config import TestConfig
from src.bookshelf.manage_users.manage_users import ManageUsers
from src.bookshelf.user import User

app, mongo = get_app_with_config(TestConfig)


class UpdateUsersTest(unittest.TestCase):

    def setUp(self):
        user_json = open('test/data/user.json')
        self.logged_user_json = json.load(user_json)
        user_json.close()
        self.manage_users = ManageUsers()
        self.manage_users.get_user = MagicMock(return_value=User(self.logged_user_json))

    def test_first_and_last_update(self):
        """
         Test update of first and last name.
         Expect to succeed and return success flash message
        """
        user = User(self.logged_user_json)
        updated_information_from_form = {
            'first_name': 'Will',
            'last_name': 'Farna'
        }
        self.manage_users.update_user_information = MagicMock(return_value=None)
        update_details = self.manage_users.update_details(user, updated_information_from_form)
        self.assertEqual(update_details["flash_message"], "Information Updated successfully")

    def test_fail_update_password_unmatching_fields(self):
        """
         Test update of password.
         Expect to return warning message and never call DB for update information
        """
        user = User(self.logged_user_json)
        updated_information_from_form = {
            'password': 'Will',
            'repeat_password': 'Farna'
        }
        update_details = self.manage_users.update_details(user, updated_information_from_form)
        self.assertEqual(update_details["flash_message"], "Password do not match, couldn't update information")

    def test_correct_update_password_matching_fields(self):
        """
         Test update of password
         Expect to succeed and return success flash message
        """
        user = User(self.logged_user_json)
        updated_information_from_form = {
            'password': 'Will',
            'repeat_password': 'Will'
        }
        self.manage_users.update_user_information = MagicMock(return_value=None)
        update_details = self.manage_users.update_details(user, updated_information_from_form)
        self.assertEqual(update_details["flash_message"], "Information Updated successfully")

    def test_update_correct_fields_db_error_response(self):
        """
         Test update of password
         Expect to succeed and return success flash message
        """
        user = User(self.logged_user_json)
        updated_information_from_form = {
            'password': 'Will',
            'repeat_password': 'Will',
            'first_name': 'Will',
            'last_name': 'Farna'
        }
        self.manage_users.update_user_information = MagicMock(return_value="Error")
        update_details = self.manage_users.update_details(user, updated_information_from_form)
        self.assertEqual(update_details["flash_message"],
                         "Something went wrong whe trying to update information, Try Again.")
