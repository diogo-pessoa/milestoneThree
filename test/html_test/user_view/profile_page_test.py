import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProfilePage(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('')
        self.driver = webdriver.Firefox(options=options)

    def tearDown(self) -> None:
        self.driver.close()

    def test_Profile_page_navigation(self):
        """
          Profile is hidden unless user is logged in

          :return:
        """
        self.driver.get("http://localhost:5000/login")
        """Fills Login Form"""
        username_tested = self.driver.find_element_by_id("username")
        username_tested.send_keys("willfarnaby")
        password_tested = self.driver.find_element_by_id("password")
        password_tested.send_keys("123")
        self.driver.find_element_by_tag_name('button').click()
        """Navigate to Profile"""
        self.driver.find_element_by_link_text('Profile').click()
        """Asserts Personal Details Tab"""
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h3"), "Will's space"),
            expected_conditions.text_to_be_present_in_element(
                (By.ID, "username"), "willfarnaby")
        )

    if __name__ == "__main__":
        unittest.main()
