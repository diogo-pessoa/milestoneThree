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
            return mongo.db.reviews.find({attribute_name: object_id})
        except IOError as e:
            print(f'ERROR - Failed to get reviews: {e}.')
            return "Error"
