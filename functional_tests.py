from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.binary_location = "/usr/bin/firefox"
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
