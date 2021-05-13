import statistics

from app import mongo
from app.model.user_model import UserModel
from src.bookshelf.review import Review


class ReviewModel(object):

    def find_user_reviews(self, user_id: str):
        """
        Queries Review by Username
        :param user_id:
        :return: list of User Objects
        """
        reviews_response = []
        reviews = mongo.db.reviews.find({"reviewer_id": user_id})

        for review in reviews:
            reviews_response.append(Review(review))
        return reviews_response

    def get_by_book_id(self, book_id):
        """
        Queries reviews by book title
        :param book_id:
        :return: list of Book Objects
        """
        reviews_response = []
        book_reviews = mongo.db.reviews.find({"book_id": book_id})
        #TODO Refactoring needed on simplify or split into separate function
        for review in book_reviews:
            review = Review(review)
            user = UserModel().find_by_id(review.get_reviewer_id())
            review.set_reviewer(user.get_first_name())
            reviews_response.append(review)
        return reviews_response

    def get_rate_by_book_id(self, book_id):
        """
            Calculates book average rate from all reviews
        :param book_id:
        :return: int() rounded rate average or 0
        """
        book_rate = []
        book_reviews = mongo.db.reviews.find({"book_id": book_id})
        for review in book_reviews:
            review = Review(review)
            book_rate.append(review.get_rate())
        if len(book_rate) == 0:
            return 0
        return round(statistics.mean(book_rate))
