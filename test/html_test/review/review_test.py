import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ReviewActions(unittest.TestCase):
    """
            Tests flow of navigation to leave a review.
            User Login
            Navigates to book page by books List (clicks on any book on the list)
            click on leave your review collapsible
            fills and Submits form, check if new review heading is showing
            then deletes review, awaits for flash message confirmation
        """

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('')
        self.driver = webdriver.Firefox(options=options)
        # Loads Login Page

    def tearDown(self):
        self.driver.close()

    def login(self):
        self.driver.get("http://0.0.0.0:5000/login")
        username_tested = self.driver.find_element_by_id("username")
        username_tested.send_keys("willfarnaby")
        password_tested = self.driver.find_element_by_id("password")
        password_tested.send_keys("123")
        self.driver.find_element_by_tag_name('button').click()

    def test_review_actions(self):
        """
            After Login creates and deletes review.
        """
        self.login()
        self.driver.find_element_by_class_name('secondary-content').click()
        self.driver.find_element_by_id("leave_review").click()
        user_review = self.driver.find_element_by_id("book_review")
        user_review.send_keys("This is the coolest book I've ever read!")
        self.driver.find_elements_by_tag_name('label')[3].click()
        # Submit review
        self.driver.find_element_by_id('submit_review_form').click()
        # Book has no reviews once one is created a new heading is added to the reviews section
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h5"), "See what others think about this book")
        )
        # Deletes Review
        self.driver.find_element_by_id('delete_review').click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "Review deleted successfully.")
        )


if __name__ == "__main__":
    unittest.main()
