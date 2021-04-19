import unittest

from selenium import webdriver


class RegisterPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_get_register_feature(self):
        driver = self.driver
        driver.get("http://localhost:5000/register")
        logo_text = driver.find_element_by_tag_name('h3').text
        self.assertEqual("Register", logo_text)
        username = driver.find_element_by_id("username")
        username.send_keys("NewUser")
        password = driver.find_element_by_id("password")
        password.send_keys("123")
        driver.find_element_by_tag_name('button')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
