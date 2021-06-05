from bson import ObjectId

from app import mongo


class BookshelfModel(object):

    def __init__(self, collection_name):
        self.collection_name = collection_name

    def search(self, query: str):
        """
        Queries Mongo Collection search Index for Book Title or Author
        :param query:
        :return: List of Book Objects matching query search or None
        """
        try:
            return mongo.db[self.collection_name].find({"$text": {"$search": query}})
        except IOError as e:
            raise Exception(f"ERROR - Search Failed: {e}.")

    def update(self, document_id: ObjectId, document_information: dict):
        """
         Update Existing book with book_information parameter content
        :param document_id:
        :param document_information:
        :return:
        """
        try:
            mongo.db[self.collection_name].update({"_id": document_id}, document_information)
        except Exception as e:
            raise Exception(f"ERROR - Failed to update document: {e}.")

    def create_one(self, new_document: dict):
        """
        Create new document in Mongo based on dict information
        :param new_document: dict
        :return: None
        """
        try:
            mongo.db[self.collection_name].insert(new_document)
        except IOError as e:
            raise Exception(f"ERROR - Failed to Create document: {e}.")

    def delete_by_id(self, document_id: ObjectId):
        """
        Deletes document based on Id, from collection_name from initialized object
        :param document_id:
        :return: None
        """
        try:
            mongo.db[self.collection_name].delete_one(document_id)
        except IOError as e:
            raise Exception(f'ERROR - Failed to delete document: {e}.')

    def find_by_id(self, object_id: str):
        """
        Searches data storage for reviews filtered by either user_id or book_id
        :param object_id: filter criteria to build list of reviews
        :return: dict: json documents
        """
        try:
            return mongo.db[self.collection_name].find_one({"_id": object_id})
        except IOError as e:
            raise Exception(f'ERROR - Failed to get document: {e}.')

    def find_by_field_name_and_value(self, value: str, field_name: str):
        """
        Looks for objects based on field name and content
        ex: reviewer_id: "hashed value"
        :param value: str
        :param field_name: str
        :return: dict: json documents
        """
        try:
            return mongo.db[self.collection_name].find({field_name: value})
        except IOError as e:
            raise Exception(f'ERROR - Failed to get document: {e}.')
