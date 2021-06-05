import statistics

from bson import ObjectId

from app.model.review_model import ReviewModel
from src.bookshelf.review import Review


class ManageReviews:

    def __init__(self):
        self.review_model = ReviewModel()

    def get_reviews(self, object_id: str, field_name: str):
        """
        Queries Data Storage for reviews, Supports either book_id or reviewer_id
        :param object_id:
        :param field_name: book_id or reviewer_id to specify which is the Id being passed to the query
        :return: dict of reviews or None
        """
        if field_name == 'reviewer_id' or field_name == 'book_id':
            reviews = []
            reviews_from_storage = self.review_model.find_reviews(object_id, field_name)
            for review in reviews_from_storage:
                reviews.append(Review(review))
            if reviews:
                return reviews
        else:
            raise Exception(f'field_name has to be either reviewer_id or book_id. Received: {field_name}')

    # reviews_response = []
    # book_reviews = mongo.db.reviews.find({"book_id": book_id})
    # # TODO Refactoring move logic to ManageReviews
    # for review in book_reviews:
    #     review = Review(review)
    #     user = UserModel().find_by_id(review.get_reviewer_id())
    #     review.set_reviewer_name(user.get_first_name())
    #     reviews_response.append(review)
    # return reviews_response

    def delete_review(self, review_id: str):
        """
            Proxy delete request to allow for mock response
        :param review_id: ObjectId
        :return: None or "Error"
        """
        delete = self.review_model.delete_review_by_id(ObjectId(review_id))
        if not delete:
            return delete

    def get_rate_by_book_id(self, book_id):
        """
            Calculates book average rate from all reviews book received
        :param book_id:
        :return: int() rounded rate average or 0
        """
        book_rate = []
        book_reviews = self.get_reviews(book_id, "book_id")
        for review in book_reviews:
            review = review
            book_rate.append(review.get_rate())
        if len(book_rate) == 0:
            return 0
        return round(statistics.mean(book_rate))

    def delete_by_review_by_id(self, review_id: str):
        """
        Checks reviewer_id matches user_id then request object deletion
        :param user_id:
        :param review_id:
        :return: response: dict
        """
        response = {
            'flash_message': "Review deleted successfully."
        }
        delete_review = self.delete_review(review_id)
        if delete_review is not None:
            response['flash_message'] = "Could Not delete review, Try Again"
        return response
