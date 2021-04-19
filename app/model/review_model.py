from app import mongo


class Review(object):

    def find_all_reviews(self):
        reviews = mongo.db.reviews.find()
        return reviews