import unittest

from selenium import webdriver


class LoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_login_page(self):
        driver = self.driver
        # Loads Login Page
        driver.get("http://localhost:5000/login")
        # Assert Login heading matches
        logo_text = driver.find_element_by_tag_name('h3').text
        self.assertEqual("Login", logo_text)
        # Interact with the form
        # username = driver.find_element_by_id("username")
        # username.send_keys("NewUser")
        # password = driver.find_element_by_id("password")
        # password.send_keys("123")
        # driver.find_element_by_tag_name('button')


if __name__ == "__main__":
    unittest.main()
