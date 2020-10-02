import unittest
from selenium import webdriver
from pages.logIn import PageLogIn
from pages.inventory import PageInventory
import time


class Example(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'D:\Documents\WebDrivers\chromedriver.exe')
        cls.driver.get('https://www.saucedemo.com/')
        cls.driver.maximize_window()
        cls.logIn = PageLogIn(cls.driver)
        cls.inventory = PageInventory(cls.driver)
    
    def test_a_log_in_with_invalid_credencials(self):
        self.logIn.log_in('locked_out_user', 'secret_sauce')
        self.assertTrue(self.logIn.error_message)

    def test_b_log_in_with_valid_credentials(self):
        self.logIn.log_in('standard_user', 'secret_sauce')
        self.assertEqual(self.driver.current_url, 'https://www.saucedemo.com/inventory.html')

    def test_c_sort_products_a_to_z(self):
        self.inventory.ordery_by_attribute('az')
        first_item = self.driver.find_element(*self.inventory.first_item_inventory).text
        self.assertEqual(first_item, 'Sauce Labs Backpack')

    def test_d_sort_products_z_to_a(self):
        self.inventory.ordery_by_attribute('za')
        first_item = self.driver.find_element(*self.inventory.first_item_inventory).text
        self.assertEqual(first_item, 'Test.allTheThings() T-Shirt (Red)')

    def test_e_sort_prodcuts_for_price_low_to_high(self):
        self.inventory.ordery_by_attribute('lohi')
        first_item = self.driver.find_element(*self.inventory.first_item_inventory).text
        self.assertEqual(first_item, 'Sauce Labs Onesie')

    def test_e_sort_prodcuts_for_price_high_to_low(self):
        self.inventory.ordery_by_attribute('hilo')
        first_item = self.driver.find_element(*self.inventory.first_item_inventory).text
        self.assertEqual(first_item, 'Sauce Labs Fleece Jacket')

    def test_f_add_four_items_to_the_cart(self):
        for i in range(3):
            self.inventory.add_new_item_to_cart(i)
            self.assertEqual(self.inventory.get_text(i), 'REMOVE')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)