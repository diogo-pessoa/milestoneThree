from bson import ObjectId

from app import mongo


class ReviewModel(object):

    @staticmethod
    def find_reviews(object_id: str, attribute_name: str):
        """
        Searches data storage for reviews filtered by either user_id or book_id
        :param object_id: filter criteria to build list of reviews
        :param attribute_name: book_id or user_id
        :return: list(Review()) or `Error`
        """
        try:
            mongo.db.reviews.find({attribute_name: object_id})
        except IOError as e:
            raise Exception(f'ERROR - Failed to get reviews: {e}.')

    @staticmethod
    def delete_review_by_id(review_id: ObjectId):
        try:
            mongo.db.reviews.delete_one(review_id)
        except IOError as e:
            raise Exception(f'ERROR - Failed to get reviews: {e}.')

    @staticmethod
    def create_review(review: dict):
        """
            Write new Review object to Data Storage
            :return: None
        """
        try:
            mongo.db.reviews.insert(review)
        except IOError as e:
            raise Exception(f"ERROR - {e}")
