import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BookNavBar(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        # Loads Login Page

    def tearDown(self):
        self.driver.close()

    def test_books_navbar_link(self):
        """
            Test Books link is show on Navbar with no action, without login session
        """
        self.driver.get("http://localhost:5000/")
        self.driver.find_element_by_link_text("Books").click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h3"), "Books")
        )

    def test_books_navbar_link_after_login(self):
        """
            Test Books link is show on Navbar with no action, with login
        """
        self.driver.get("http://localhost:5000/login")
        # Interact with the form
        username_tested = self.driver.find_element_by_id("username")
        username_tested.send_keys("willfarnaby")
        password_tested = self.driver.find_element_by_id("password")
        password_tested.send_keys("123")
        self.driver.find_element_by_tag_name('button').click()
        book_dropdown_button = self.driver.find_element_by_id("dropdown-nav-main")
        self.assertIsNotNone(book_dropdown_button)


if __name__ == "__main__":
    unittest.main()
