import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProfilePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self) -> None:
        self.driver.close()

    def test_Profile_page_after_login(self):
        self.driver.get("http://localhost:5000/login")
        # Login
        username_tested = self.driver.find_element_by_id("username")
        username_tested.send_keys("newuser")
        password_tested = self.driver.find_element_by_id("password")
        password_tested.send_keys("123")
        self.driver.find_element_by_tag_name('button').click()
        self.driver.find_element_by_link_text('Profile').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h3"), "Newuser")
        )


if __name__ == "__main__":
    unittest.main()
