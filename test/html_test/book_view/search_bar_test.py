import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchBar(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        # Loads Login Page
        self.driver.get("http://localhost:5000/book")

    def tearDown(self):
        self.driver.close()

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
        book_title = self.driver.find_element_by_id("query")
        book_title.send_keys("Nothing to be found")
        self.driver.find_element_by_tag_name('button').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "No books found for this search.")
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
