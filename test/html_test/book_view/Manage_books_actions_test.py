import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AddBookPage(unittest.TestCase):
    """
        Tests flow of navigation to add new book.
        Simulates users Login
        Navigation to new book form by dropdown link.
        Fills form with fake content.
        Submits form, awaits for flash message confirmation
        then submit a delete action from book page, waiting from flash message confirmation
    """

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)

    def tearDown(self):
        self.driver.close()

    def login(self):
        self.driver.get("http://0.0.0.0:5000/login")
        username_tested = self.driver.find_element_by_id("username")
        username_tested.send_keys("willfarnaby")
        password_tested = self.driver.find_element_by_id("password")
        password_tested.send_keys("123")
        self.driver.find_element_by_tag_name('button').click()

    def test_add_without_login_session_redirects_to_login(self):
        self.driver.get("http://0.0.0.0:5000/book/new")
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "Login to execute this operation"),
        )

    def test_add_delete_book(self):
        """
            Open add new book form, Create new book, delete book
        """
        self.login()
        # Navigates to Add new book form page
        self.driver.find_element_by_link_text('Books\narrow_drop_down').click()
        self.driver.find_element_by_link_text('add\nAdd').click()

        # Fills Form
        title = self.driver.find_element_by_id('title')
        title.send_keys('new book')
        description = self.driver.find_element_by_id('description')
        description.send_keys('this is a new book on this cool website')
        author = self.driver.find_element_by_id('author')
        author.send_keys('Jon Doe')
        released_date = self.driver.find_element_by_id('released_date')
        released_date.send_keys('2020')
        publisher = self.driver.find_element_by_id('released_date')
        publisher.send_keys('no need')
        category = self.driver.find_element_by_id('category')
        category.send_keys('New')
        edition = self.driver.find_element_by_id('edition')
        edition.send_keys('1')
        # Submit form
        self.driver.find_element_by_tag_name('button').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "New Book added!")
        )

        # Delete book
        self.driver.find_element_by_tag_name('button').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "Book Removed")
        )

if __name__ == "__main__":
    unittest.main()
