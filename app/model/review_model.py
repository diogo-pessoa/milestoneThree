import statistics

from app import mongo
from src.bookshelf.review import Review


class ReviewModel(object):

    def find_all_user_reviews(self, username: str):
        """
        Queries Review by Username
        :param username:
        :return: list of User Objects
        """
        reviews_response = []
        reviews = mongo.db.reviews.find({"reviewer": username})

        for review in reviews:
            reviews_response.append(Review(review))
        return reviews_response

    def find_all_book_reviews(self, book_title):
        """
        Queries reviews by book title
        :param book_title:
        :return: list of Book Objects
        """
        reviews_response = []
        book_reviews = mongo.db.reviews.find({"book": book_title})
        for review in book_reviews:
            reviews_response.append(Review(review))
        return reviews_response

    def get_book_rate_by_title(self, book_title):
        """
            Calculates book average rate from all reviews
        :param book_title:
        :return: int() rounded rate average or 0
        """
        book_rate = []
        book_reviews = mongo.db.reviews.find({"book": book_title})
        for review in book_reviews:
            review = Review(review)
            book_rate.append(review.get_rate())
        if len(book_rate) == 0:
            return 0
        return round(statistics.mean(book_rate))
