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

    def test_edit_without_login_session_redirects_to_login(self):
        self.driver.get("http://0.0.0.0:5000/book/edit/60773a16cb838494e13d3652")
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "Login to execute this operation"),
        )

    def test_edit_page_form_fields(self):
        # Interact with the form
        self.driver.get("http://0.0.0.0:5000/login")
        username_tested = self.driver.find_element_by_id("username")
        username_tested.send_keys("NewUser")
        password_tested = self.driver.find_element_by_id("password")
        password_tested.send_keys("123")
        self.driver.find_element_by_tag_name('button').click()
        self.driver.get("http://0.0.0.0:5000/book/edit/60773a16cb838494e13d3652")

        title = self.driver.find_element_by_id('title')
        self.assertIsNotNone(title)
        title = self.driver.find_element_by_id('title').get_property('value')
        self.assertEqual('Book  12', title)
        author = self.driver.find_element_by_id('author').get_property('value')
        self.assertEqual('Jon Doe', author)


if __name__ == "__main__":
    unittest.main()
