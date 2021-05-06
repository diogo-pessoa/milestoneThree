import unittest

from selenium import webdriver


class TheBookShelfMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:5000")

    def tearDown(self):
        self.driver.close()

    def test_get_index_page(self):
        self.assertIn('Bookshelf', self.driver.title)
        logo_text = self.driver.find_element_by_class_name('brand-logo').text
        self.assertEqual("Bookshelf", logo_text)


if __name__ == "__main__":
    unittest.main()
