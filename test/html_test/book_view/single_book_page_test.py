import unittest

from selenium import webdriver


class BookPage(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        # Loads Login Page
        self.driver.get("http://localhost:5000/book/book--12")

    def tearDown(self):
        self.driver.close()

    def test_book_page_title(self):
        book_title = self.driver.find_element_by_tag_name('h3').text
        self.assertEqual("Book 12", book_title)

    def test_book_page_buttons(self):
        share_button = self.driver.find_element_by_link_text('send\nSHARE').text
        self.assertIsNotNone(share_button)
        find_store_button = self.driver.find_element_by_link_text('local_library\nFIND IN STORE').text
        self.assertIsNotNone(find_store_button)

    def test_review_section(self):
        """
        Book 12 Has one review on test DB, expect to show reviews
        Looks for element in review card
        :return:
        """
        user_comment = self.driver.find_element_by_tag_name('blockquote')
        self.assertIsNotNone(user_comment)

    def test_review_section_for_book_with_no_reviews(self):
        """
        Book has no reviews, expects to show no review message
        :return:
        """
        self.driver.get("http://0.0.0.0:5000/book/how-to-kill-a-mockingbird")
        no_review_heading = self.driver.find_element_by_id('no_review').text

        self.assertEqual("No Reviews yet :/", no_review_heading)


if __name__ == "__main__":
    unittest.main()
