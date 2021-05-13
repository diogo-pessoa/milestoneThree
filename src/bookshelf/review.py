from bson import ObjectId


class Review:

    def __init__(self, review: dict):
        if review:
            self.__feedback = review.get('feedback')
            self.__book_id = ObjectId(review.get('book_id'))
            self.__reviewer_id = ObjectId(review.get('reviewer_id'))
            self.__rate = review.get('rate')
            self.__reviewer = ""

    def get_rate(self):
        return int(self.__rate)

    def get_feedback(self):
        return self.__feedback

    def get_reviewer_id(self):
        return self.__reviewer_id

    def set_reviewer(self, username: str):
        self.__reviewer = username

    def get_reviewer(self):
        return self.__reviewer

    def get_dict(self):
        return {
            "feedback": self.get_feedback(),
            "book_id": self.__book_id,
            "reviewer_id": self.get_reviewer_id(),
            "rate": self.get_rate()
        }
