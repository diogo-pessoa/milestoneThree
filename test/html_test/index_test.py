import unittest

from selenium import webdriver


class TheBookShelfMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_get_log_text_from_index(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        self.assertIn('Bookshelf', driver.title)
        logo_text = driver.find_element_by_class_name('brand-logo').text
        self.assertEqual("Bookshelf", logo_text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()