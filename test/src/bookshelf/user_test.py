import json
import unittest

from src.bookshelf.user import User


class UserTest(unittest.TestCase):

    def setUp(self):
        file = open('test/data/user.json')
        self.user = User(json.load(file))
        file.close()

    def test_get_username(self):
        self.assertEqual('willfarnaby', self.user.get_username())

    def test_get_user_first_name(self):
        self.assertEqual('Will', self.user.get_first_name())

    def test_get_user_last_name(self):
        self.assertEqual('Farnaby', self.user.get_last_name())

    def test_get_favorite_books(self):
        favorite_books = self.user.get_favorite_books()
        self.assertIn("A book", favorite_books)
        self.assertEqual(2, len(favorite_books))

if __name__ == "__main__":
    unittest.main()
