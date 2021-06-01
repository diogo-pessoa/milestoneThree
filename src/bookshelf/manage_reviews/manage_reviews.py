from app.model.book_model import BookModel
from app.model.review_model import ReviewModel
from src.bookshelf.manage_users.manage_users import ManageUsers
from src.bookshelf.review import Review


class ManageReviews:

    def __init__(self):
        self.review_model = ReviewModel()

    def get_reviews(self, object_id: str, field_name: str):
        """
        Queries Data Storage for reviews, Supports either book_id or reviewer_id
        :param object_id:
        :param field_name: book_id or reviewer_id to specify which is the Id being passed to the query
        :return: dict of reviews
        """
        reviews = []
        for review in self.review_model.find_reviews(object_id, field_name):
            reviews.append(Review(review))
        return reviews

    def get_by_user(self, user_id: str):
        """
            queries data storage and return
            :param: username: str
            :return: list of Review instances
        """
        user_name = ManageUsers().get_by_id(user_id)
        user_name = user_name.get_first_name()
        user_reviews = []
        collection_name = 'users'
        reviews_from_db = self.get_reviews(user_id, collection_name)
        if reviews_from_db:
            for review in reviews_from_db:
                single_review = review
                # Query_book_title_by_id
                # TODO move to private method
                book_in_list = BookModel().find_by_id(single_review.get_book_id())
                # Set attributes value to review
                single_review.set_book_title(book_in_list.get_formatted_title())
                single_review.set_reviewer_name(user_name)
                user_reviews.append(single_review)
        return user_reviews

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
