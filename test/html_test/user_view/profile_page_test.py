import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProfilePage(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)

    def login(self):
        self.driver.get("https://the-bookshelf-milestone-three.herokuapp.com/login")
        username_tested = self.driver.find_element_by_id("username")
        username_tested.send_keys("willfarnaby")
        password_tested = self.driver.find_element_by_id("password")
        password_tested.send_keys("123")
        self.driver.find_element_by_tag_name('button').click()

    def tearDown(self) -> None:
        self.driver.close()

    def test_Profile_page_navigation(self):
        """
          Navigates to Profile page, confirm user information is loaded on Tabs

        """
        # Login
        self.login()
        # navigate to user profile
        self.driver.find_element_by_link_text('Profile').click()
        # Checks for title and Tabs
        page_title = self.driver.find_element_by_tag_name("h3").text
        self.assertEqual("Will's space", page_title)
        # Asserts Personal Details Tab
        username_in_form = self.driver.find_element_by_id("username").get_property('value')
        self.assertEqual("willfarnaby", username_in_form)
        # Assert Reviews tabs is visible
        review_tab = self.driver.find_element_by_link_text('REVIEWS')
        self.assertIsNotNone(review_tab)
        # Asserts books favorites is there and link works
        self.driver.find_element_by_link_text('MY FAVORITES').click()
        self.driver.find_element_by_link_text('Modern Operating Systems').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h3"), "Modern Operating Systems")
        )

    if __name__ == "__main__":
        unittest.main()
