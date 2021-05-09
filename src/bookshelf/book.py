from bson.objectid import ObjectId


class Book:

    def __init__(self, book: dict):
        if book:
            self.__id = ObjectId(book.get('_id'))
            self.__title = book.get('title')
            self.__author = book.get('author')
            self.__publisher = book.get('publisher')
            self.__release_date = book.get("released")
            self.__reviewed = book.get("reviewed")
            self.__edition = book.get("edition")
            self.__category = book.get("category")
            self.__cover_image = book.get("cover_image")
            self.__description = book.get("description")

    def get_id(self):
        return self.__id

    def get_title(self):
        title = self.__title
        return title.capitalize()

    def get_title_for_url(self):
        title = self.__title.replace(" ", "")
        return title.lower()

    def get_author(self):
        return self.__author or "Not Informed"

    def get_publisher(self):
        return self.__publisher or "Not Informed"

    def get_release_date(self):
        return self.__release_date or "Not Informed"

    def get_reviewed(self):
        if int(self.__reviewed) == 1:
            return True
        return False

    def get_edition(self):
        return self.__edition or "Not Informed"

    def get_category(self):
        return self.__category or "general"

    def get_cover_image(self):
        return self.__cover_image

    def get_description(self):
        return self.__description or "empty"

    def get_dict(self):
        return {
            "title": self.get_title(),
            "author": self.get_author(),
            "publisher": self.get_publisher(),
            "released_date": self.get_release_date(),
            "reviewed": self.get_reviewed(),
            "edition": self.get_edition(),
            "category": self.get_category(),
            "cover_image": self.get_cover_image(),
            "description": self.get_description()
        }
