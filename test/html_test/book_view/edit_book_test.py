import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class EditBookPage(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)

    def tearDown(self):
        self.driver.close()

    def login(self):
        self.driver.get("https://the-bookshelf-milestone-three.herokuapp.com/login")
        username_tested = self.driver.find_element_by_id("username")
        username_tested.send_keys("willfarnaby")
        password_tested = self.driver.find_element_by_id("password")
        password_tested.send_keys("123")
        self.driver.find_element_by_tag_name('button').click()

    def test_login_required_for_edit_book_page(self):
        """
            Expects only logged users to open edit page, otherwise redirect to Login
        """
        self.driver.get("https://the-bookshelf-milestone-three.herokuapp.com/book/edit/60773a16cb838494e13d3654")
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "Login to execute this operation"),
        )

    def test_edit_page_form_fields(self):
        """
            Checks pages edit loads properly, and fields are pre-populated

        """
        # Login
        self.login()
        # Navigate to book page
        self.driver.get("https://the-bookshelf-milestone-three.herokuapp.com/book/modern-operating-systems")

        # Go to Edit Action
        self.driver.find_element_by_link_text('ACTIONS\narrow_drop_down').click()
        self.driver.find_element_by_link_text('edit\nEdit').click()

        title = self.driver.find_element_by_id('title')
        self.assertIsNotNone(title)
        title = self.driver.find_element_by_id('title').get_property('value')
        self.assertEqual('Modern Operating Systems', title)
        author = self.driver.find_element_by_id('author').get_property('value')
        self.assertEqual('Andrew Tanenbaum, Herbert Bos', author)


if __name__ == "__main__":
    unittest.main()
