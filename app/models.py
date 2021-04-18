from app import mongo


class Data(object):

    def find_all_books(self):
        return mongo.db.books.find()


    def find_all_reviews(self):
        reviews = mongo.db.reviews.find()
        return reviews

    def find_user_by_name(self, name):
        user = mongo.db.users.find_one({"username": name})
        return user.get("username")