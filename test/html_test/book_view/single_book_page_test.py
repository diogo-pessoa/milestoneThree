import unittest

from selenium import webdriver


class LoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # Loads Login Page
        self.driver.get("http://localhost:5000/book/book1")

    def tearDown(self):
        self.driver.close()

    def test_book_page_title(self):
        book_title = self.driver.find_element_by_tag_name('h3').text
        self.assertEqual("Book1", book_title)

    def test_book_page_buttons(self):
        self.driver.find_element_by_link_text('send\nSHARE').text
        self.driver.find_element_by_link_text('local_library\nFIND IN STORE').text
        self.driver.find_element_by_link_text('rate_review\nREVIEW THIS BOOK').text


if __name__ == "__main__":
    unittest.main()
