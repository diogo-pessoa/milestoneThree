import unittest

from selenium import webdriver


class BookPage(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        # Loads Login Page
        self.driver.get("http://localhost:5000/book/book1")

    def tearDown(self):
        self.driver.close()

    def test_book_page_title(self):
        book_title = self.driver.find_element_by_tag_name('h3').text
        self.assertEqual("Book1", book_title)

    def test_book_page_buttons(self):
        share_button = self.driver.find_element_by_link_text('send\nSHARE').text
        self.assertIsNotNone(share_button)
        find_store_button = self.driver.find_element_by_link_text('local_library\nFIND IN STORE').text
        self.assertIsNotNone(find_store_button)
        review_button = self.driver.find_element_by_link_text('rate_review\nREVIEW THIS BOOK').text
        self.assertIsNotNone(review_button)


if __name__ == "__main__":
    unittest.main()
