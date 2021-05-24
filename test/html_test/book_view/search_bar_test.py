import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchBar(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('')
        self.driver = webdriver.Firefox(options=options)
        self.driver.get("http://localhost:5000/book")

    def tearDown(self):
        self.driver.close()

    def login(self):
        self.driver.get("http://0.0.0.0:5000/login")
        username_tested = self.driver.find_element_by_id("username")
        username_tested.send_keys("willfarnaby")
        password_tested = self.driver.find_element_by_id("password")
        password_tested.send_keys("123")
        self.driver.find_element_by_tag_name('button').click()

    def test_search_bar_text_content(self):
        search_bar_text = self.driver.find_element_by_tag_name('label').text
        self.assertEqual("Type a book title or author Name", search_bar_text)

    def test_book_page_buttons(self):
        reset_button_text = self.driver.find_element_by_link_text('RESET').text
        search_button_text = self.driver.find_element_by_tag_name('button').text
        self.assertEqual("RESET", reset_button_text)
        self.assertEqual("SEARCH", search_button_text)

    def test_search_for_book_1(self):
        book_title = self.driver.find_element_by_id("query")
        book_title.send_keys("Book 12")
        self.driver.find_element_by_tag_name('button').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.CLASS_NAME, "title"), "Book 12")
        )

    def test_search_no_matching_result(self):
        """
            Runs a search for with a book that doesn't exist,
            response should inform no book was found and redirect user to register if not logged in
        :return:
        """
        book_title = self.driver.find_element_by_id("query")
        book_title.send_keys("Nothing to be found")
        self.driver.find_element_by_tag_name('button').click()
        no_books = self.driver.find_element_by_tag_name('h4').text
        self.assertEqual("No books found for this search.", no_books)
        self.driver.find_element_by_link_text('Register Now').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h3"), "Register")
        )

    def test_search_no_matching_result_logged_in(self):
        """
            Runs a search for with a book that doesn't exist,
            response should inform no book was found and redirect user to create new book
            :return:
        """
        # Login
        self.login()
        # query for book
        book_title = self.driver.find_element_by_id("query")
        book_title.send_keys("Nothing to be found")
        self.driver.find_element_by_tag_name('button').click()
        # click on create new book link
        self.driver.find_element_by_link_text('Create new book').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h5"), "About This Book")
        )

    def test_search_by_author(self):
        book_title = self.driver.find_element_by_id("query")
        book_title.send_keys("Jon Doe")
        self.driver.find_element_by_tag_name('button').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "p"), "By Jon Doe")
        )


if __name__ == "__main__":
    unittest.main()
