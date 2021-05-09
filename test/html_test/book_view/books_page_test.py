import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BooksPage(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        # Loads Login Page
        self.driver.get("http://localhost:5000/book")

    def tearDown(self):
        self.driver.close()

    def test_books_list_page(self):
        heading = self.driver.find_element_by_tag_name('h3').text
        self.assertEqual("Books", heading)
        book_title = self.driver.find_element_by_class_name('title').text
        self.assertEqual("Book1", book_title)

    def test_see_more_link_on_books_list(self):
        self.driver.get("http://localhost:5000/book")
        self.driver.find_element_by_class_name('secondary-content').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h5"), "About This Book")
        )


if __name__ == "__main__":
    unittest.main()
