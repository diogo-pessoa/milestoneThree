from bson import ObjectId

from app.model.review_model import ReviewModel


class ManageReviews:

    def __init__(self):
        self.review_model = ReviewModel()

    def get_reviews_user_id(self, user_id: ObjectId):
        """
            queries data storage and return User() instance
            :param: username: str
            :return: Review()
        """
        collection_name = 'users'
        return self.review_model.find_reviews(user_id, collection_name)

    def get_reviews_by_book(self, book_id):
        """
            queries data storage and return User() instance
            :param: username: str
            :return: User() Object with data from data storage
        """
        collection_name = 'books'
        return self.review_model.find_reviews(book_id, collection_name)

    # def create_new(self, book_id: ObjectId, user_id: ObjectId, book_rate: int, book_review: str, ):
    #     pass
    #     # TODO return flash message
