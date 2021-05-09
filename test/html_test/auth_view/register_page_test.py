import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegisterPage(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        self.driver.get("http://localhost:5000/register")

    def tearDown(self):
        self.driver.close()

    def test_register_page(self):
        # Assert Register heading matches
        logo_text = self.driver.find_element_by_tag_name('h3').text
        self.assertEqual("Register", logo_text)

        # Interact with the Register form
        username = self.driver.find_element_by_id("username")
        username.send_keys("NewUser")
        password = self.driver.find_element_by_id("password")
        password.send_keys("123")
        self.driver.find_element_by_tag_name('button').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "username already in use")
        )

    def test_go_to_login_from_register(self):
        self.driver.find_element_by_link_text("Sign-up").click()
        self.driver.find_element_by_link_text("Log In").click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h3"), "Login")
        )

if __name__ == "__main__":
    unittest.main()
