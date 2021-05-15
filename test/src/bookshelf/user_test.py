import json
import unittest

from src.bookshelf.user import User


class UserTest(unittest.TestCase):

    def setUp(self):
        file = open('test/data/user.json')
        user_data = json.load(file)
        file.close()
        self.user = User(user_data)

    def test_get_username(self):
        self.assertEqual('willfarnaby', self.user.get_username())

    def test_get_user_first_name(self):
        self.assertEqual('William', self.user.get_first_name())

    def test_get_user_last_name(self):
        self.assertEqual('Farnaby', self.user.get_last_name())

    def test_get_favorite_books(self):
        favorite_books = self.user.get_favorite_books()
        self.assertIn("A book", favorite_books)
        self.assertEqual(2, len(favorite_books))

    def test_is_moderator(self):
        self.assertFalse(self.user.is_moderator())

    def test_check_password(self):
        given_password = "randomHashed Pass"
        self.user.__set_password(given_password)
        self.assertTrue(self.user.check_password(given_password))

    def test_get_dict(self):
        user_repr = self.user.get_dict()
        self.assertEqual("willfarnaby", user_repr['username'])
        self.assertFalse(user_repr['moderator'])

    def test_update_details(self):
        user_repr = self.user
        updated_information = {
            'first_name': 'Will',
            'last_name': 'Farna'
        }

        user_repr.update_details(updated_information)
        self.assertEqual(updated_information.get('first_name'), self.user.get_first_name())
        self.assertEqual(updated_information.get('last_name'), self.user.get_last_name())

    def test_update_password(self):
        user_repr = self.user
        updated_information = {
            'password': '123qwe',
            'repeat_password': '123qwe'}
        user_repr.update_details(updated_information)
        self.assertTrue(user_repr.check_password('123qwe'))

    def test_update_password_raise_exception(self):
        """
        In case passwords do not match, it is critical to raise exception

        """
        user_repr = self.user
        updated_information = {
            'password': '123qwe',
            'repeat_password': '123qw'}
        user_repr.update_details(updated_information)
        self.assertTrue(user_repr.check_password('123qwe'))


if __name__ == "__main__":
    unittest.main()
