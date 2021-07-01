import unittest

from selenium import webdriver


class BookPage(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        self.driver.get("https://the-bookshelf-milestone-three.herokuapp.com/book/modern-operating-systems")

    def tearDown(self):
        self.driver.close()

    def test_book_page_title_description(self):
        book_title = self.driver.find_element_by_tag_name('h3').text
        about_book = self.driver.find_element_by_tag_name('p').text
        self.assertEqual("Modern Operating Systems", book_title)
        self.assertIn("Modern Operating Systems", about_book)

    def test_book_page_buy_now_button(self):
        """
            check if buy now button still shows for not logged in user

        """

        buy_now = self.driver.find_element_by_link_text('local_library BUY NOW')
        self.assertIsNotNone(buy_now)

    def test_review_section_for_book_with_no_reviews(self):
        """
        Book has no reviews, expects to show no review message
        """
        no_review_heading = self.driver.find_element_by_id('no_review').text
        self.assertEqual("No Reviews yet :/", no_review_heading)


if __name__ == "__main__":
    unittest.main()
