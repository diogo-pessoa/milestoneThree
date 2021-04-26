import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # Loads Login Page
        self.driver.get("http://localhost:5000/login")

    def tearDown(self):
        self.driver.close()

    def test_login_page(self):
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

    def test_login_functionality(self):
        # Interact with the form
        username_tested = self.driver.find_element_by_id("username")
        username_tested.send_keys("NewUser")
        password_tested = self.driver.find_element_by_id("password")
        password_tested.send_keys("123")
        self.driver.find_element_by_tag_name('button').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "Welcome, NewUser"),
            # checks if NavBar is updated with conditional Log Out element
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "a"), "Log out")
        )
        # Clicks Log out element
        self.driver.find_element_by_link_text('Log out').click()
        login = self.driver.find_element_by_link_text('Login')
        # checks if Element Login is once again added to Navbar after logout
        self.assertEqual(login.text, "Login")

        if __name__ == "__main__":
            unittest.main()
