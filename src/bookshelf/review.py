class Review:

    def __init__(self, review: dict):
        if review:
            self.__feedback = review.get('feedback')
            self.__book = review.get('book')
            self.__reviewer = review.get('reviewer')
            self.__rate = review.get('rate')

    def get_rate(self):
        return self.__rate

    def get_book(self):
        return self.__book

    def get_reviewer(self):
        return self.__reviewer

    def get_feedback(self):
        return self.__feedback

    def get_dict(self):
        return {
            "feedback": self.get_feedback(),
            "book": self.get_book(),
            "reviewer": self.get_reviewer(),
            "rate": self.get_rate()
        }
