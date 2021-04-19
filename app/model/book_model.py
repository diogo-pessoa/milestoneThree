from app import mongo


class Book(object):

    def find_all_books(self):
        return mongo.db.books.find()