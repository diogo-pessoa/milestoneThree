from app import mongo
from src.bookshelf.review import Review


class ReviewModel(object):

    def find_all_user_reviews(self, username: str):
        reviews_response = []
        reviews = mongo.db.reviews.find({"reviewer": username})

        for review in reviews:
            print(review)
            reviews_response.append(Review(review))
        return reviews_response
