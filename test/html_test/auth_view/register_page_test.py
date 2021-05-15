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

    def tearDown(self):
        self.driver.close()

    def test_form_field_and_button(self):
        """
        Test Register page form elements content and text
        :return: None
        """
        self.driver.get("http://localhost:5000/register")
        logo_text = self.driver.find_element_by_tag_name('h3').text
        self.assertEqual("Register", logo_text)
        # Check Button
        form_button = self.driver.find_element_by_tag_name('button')
        self.assertEqual("REGISTER check", form_button.text)

    def test_register_form_user_exists(self):
        """
        Fill form content and click button
        :Expect: to flash warn that username is in use
        """
        self.driver.get("http://localhost:5000/register")
        # Interact with the Register form
        username = self.driver.find_element_by_id("username")
        username.send_keys("NewUser")
        password = self.driver.find_element_by_id("password")
        password.send_keys("123")
        password = self.driver.find_element_by_id("repeat-password")
        password.send_keys("123")
        # button field
        self.driver.find_element_by_tag_name('button').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "username already in use")
        )

    def test_register_form_pass_do_not_match(self):
        self.driver.get("http://localhost:5000/register")
        # Interact with the Register form
        username = self.driver.find_element_by_id("username")
        username.send_keys("yetanothernewuser")
        password = self.driver.find_element_by_id("password")
        password.send_keys("123")
        password = self.driver.find_element_by_id("repeat-password")
        password.send_keys("124")
        # button field
        self.driver.find_element_by_tag_name('button').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "Passwords do not match")
        )

    def test_go_to_login_from_register(self):
        """
        Test Login link on bottom of form
        """
        self.driver.get("http://localhost:5000/register")
        self.driver.find_element_by_link_text("Sign-up").click()
        self.driver.find_element_by_link_text("Log In").click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h3"), "Login")
        )


if __name__ == "__main__":
    unittest.main()
