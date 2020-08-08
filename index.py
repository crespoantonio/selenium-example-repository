import unittest
from selenium import webdriver
from pages.logIn import PageLogIn


class Example(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()
        self.logIn = PageLogIn(self.driver)
    
    def test_a(self):
        self.logIn.log_in('standard_user', 'secret_sauce')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()