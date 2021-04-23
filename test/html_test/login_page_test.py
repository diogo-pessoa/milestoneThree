import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_login_page(self):
        self.driver
        # Loads Login Page
        self.driver.get("http://localhost:5000/login")
        # Assert Login heading matches
        logo_text = self.driver.find_element_by_tag_name('h3').text
        self.assertEqual("Login", logo_text)
        # Interact with the form
        username = self.driver.find_element_by_id("username")
        username.send_keys("NewUser")
        password = self.driver.find_element_by_id("password")
        password.send_keys("1234")
        self.driver.find_element_by_tag_name('button').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "Invalid Credentials")
        )

    def test_login_page_cookie(self):
        # Loads Login Page
        self.driver.get("http://localhost:5000/login")
        # Interact with the form
        username_tested = self.driver.find_element_by_id("username")
        username_tested.send_keys("NewUser")
        password_tested = self.driver.find_element_by_id("password")
        password_tested.send_keys("123")
        self.driver.find_element_by_tag_name('button').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "Welcome, NewUser")
        )



if __name__ == "__main__":
    unittest.main()
