import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class EditBookPage(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        # Loads Login Page
        self.driver.get("http://localhost:5000/book")

    def tearDown(self):
        self.driver.close()

    def test_edit_without_login_session_redirects_to_login(self):
        self.driver.get("http://0.0.0.0:5000/book/edit/60773a16cb838494e13d3652")
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h4"), "Login to execute this operation"),
        )


if __name__ == "__main__":
    unittest.main()
