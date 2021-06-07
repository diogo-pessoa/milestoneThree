import statistics

from bson import ObjectId

from app.model.bookshelf_model import BookshelfModel
from src.bookshelf.book import Book
from src.bookshelf.manage_users.manage_users import ManageUsers
from src.bookshelf.review import Review
from src.bookshelf.user import User


class ManageReviewSuper:
    """
        Super Class wrapping DataStorage calls for reviews documents
    """

    def __init__(self):
        self.model = BookshelfModel('reviews')

    def get_review_by_value_and_field(self, value: str, field_name: str):
        """

        :param value: ex: book_id
        :param field_name: ex: 'fdaspnmasdnfas1234'
        :return: Single Review instance
        """
        review = self.model.find_by_field_name_and_value(value, field_name)
        if review:
            return Review(review)

    def get_many(self, object_id: str, field_name: str):
        """
        Queries Data Storage for reviews, Supports either book_id or reviewer_id
        :param object_id:
        :param field_name: book_id or reviewer_id to specify which is the Id being passed to the query
        :return: dict of reviews or None
        """
        if field_name == 'reviewer_id' or field_name == 'book_id':
            reviews = []
            reviews_from_storage = self.model.find_many_by_field_name_and_value(object_id, field_name)
            for review in reviews_from_storage:
                reviews.append(Review(review))
            if reviews:
                return reviews
        else:
            raise Exception(f'field_name has to be either reviewer_id or book_id. Received: {field_name}')

    def create(self, review: Review):
        """
            Wrapper call for data storage Class
        :param review:
        :return: None
        """
        create = self.model.create_one(review.get_dict())
        if not create:
            return create

    def delete(self, review_id: str):
        """
            Proxy delete request to allow for mock response
        :param review_id: ObjectId

        """
        self.model.delete_by_id(ObjectId(review_id))

    def get_by_id(self, review_id: str):
        """
        Gets single review based on review_id
        :param review_id:
        :return: Review:
        """
        review = self.model.find_by_id(ObjectId(review_id))
        if review:
            return Review(review)


class ManageReviews(ManageReviewSuper):
    """
        manage to handles Book Reviews
    """

    def __init__(self):
        super().__init__()
        self.manage_users = ManageUsers()

    def get_rate_by_book_id(self, book_id: str):
        """
            Calculates book average rate from all reviews book received
        :param book_id:
        :return: int() rounded rate average or 0
        """
        book_rate = []
        book_reviews = self.get_many(book_id, "book_id")
        if book_reviews:
            for review in book_reviews:
                review = review
                book_rate.append(review.get_rate())
            if len(book_rate) == 0:
                return 0
            return round(statistics.mean(book_rate))
        else:
            return 0

    def delete_review_by_id(self, review_id: str):
        """
        Delete Review by Id, then returns flash message and book_title
        :param review_id: str
        :return: response: dict
        """
        response = {
            'flash_message': "Could Not delete review, Try Again",
            'book_id': ''
        }
        review = self.get_by_id(review_id)
        book_id = review.get_book_id()
        self.delete(review_id)
        response['flash_message'] = 'Review deleted successfully.'
        response['book_id'] = review.get_book_id()
        return response

    def add_new_review(self, book: Book, user: User, book_rate: int, book_review: str):
        """
        Adds new review from dict with information passed from web form
        :param book:
        :param user:
        :param book_rate:
        :param book_review:
        :return: response with flash message
        """
        response = {
            "flash_message": "Review created successfully."
        }
        review = Review({
            'book_id': ObjectId(book),
            'rate': book_rate,
            'reviewer_id': ObjectId(user),
            'feedback': book_review
        })
        create_review = self.create(review)
        if create_review is not None:
            response['flash_message'] = "Could Not create review, Try Again"
        return response

    def get_reviews(self, value: str, field_name: str):
        """
        Queries Data Storage for reviews, Supports either book_id or reviewer_id
        :param value:
        :param field_name: book_id or reviewer_id to specify which is the Id being passed to the query
        :return: dict of reviews or None
        """
        if field_name == 'reviewer_id' or field_name == 'book_id':
            reviews = []
            reviews_from_storage = self.get_many(value, field_name)
            if reviews_from_storage:
                for review in reviews_from_storage:
                    review.get_reviewer_id()
                    user_name = self.manage_users.get_by_id(review.get_reviewer_id())
                    if user_name:
                        review.set_reviewer_name(user_name.get_first_name())
                    else:
                        review.set_reviewer_name("Not a user anymore")
                    reviews.append(review)
                    print(review)
                return reviews
        else:
            raise Exception(f'field_name has to be either reviewer_id or book_id. Received: {field_name}')
        return reviews
