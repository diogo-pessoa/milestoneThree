import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_get_heading_content(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        heading_one_text = (driver.find_element_by_tag_name('h1').text)
        self.assertEqual("Welcome", heading_one_text )

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()