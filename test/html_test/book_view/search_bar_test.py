import unittest

from selenium import webdriver


class SearchBar(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        # Loads Login Page
        self.driver.get("http://localhost:5000/book")

    def tearDown(self):
        self.driver.close()

    def test_text_element_content(self):
        search_bar_text = self.driver.find_element_by_tag_name('label').text
        self.assertEqual("Type a book title or author Name", search_bar_text)

    def test_book_page_buttons(self):
        reset_button_text = self.driver.find_element_by_link_text('RESET').text
        search_button_text = self.driver.find_element_by_tag_name('button').text
        self.assertEqual("RESET", reset_button_text)
        self.assertEqual("SEARCH", search_button_text)


if __name__ == "__main__":
    unittest.main()
