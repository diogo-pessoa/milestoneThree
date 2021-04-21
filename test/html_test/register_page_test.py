import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegisterPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_register_page(self):
        driver = self.driver
        driver.get("http://localhost:5000/register")

        # Assert Register heading matches
        logo_text = driver.find_element_by_tag_name('h3').text
        self.assertEqual("Register", logo_text)

        # Interact with the Register form
        username = driver.find_element_by_id("username")
        username.send_keys("NewUser")
        password = driver.find_element_by_id("password")
        password.send_keys("123")
        driver.find_element_by_tag_name('button').click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "username already in use")
        )
        driver.close()


if __name__ == "__main__":
    unittest.main()
