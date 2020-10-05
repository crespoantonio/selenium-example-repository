from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver

class PageInventory():
    def __init__(self, driver):
        self.driver = driver
        self.btn_menu = (By.CSS_SELECTOR, '#menu_button_container div:nth-child(3) button')
        self.div_menu_side_right =(By.CLASS_NAME, 'bm-menu')
        self.a_all_items = (By.ID, 'inventory_sidebar_link')
        self.a_logout = (By.ID, 'logout_sidebar_link')
        self.a_reset_app = (By.ID, 'reset_sidebar_link')
        self.first_item_inventory = (By.CSS_SELECTOR, '.inventory_list > :nth-child(1) .inventory_item_name')
        self.select_product_sort_container = (By.CLASS_NAME, 'product_sort_container')
        self.find_item = (By.CSS_SELECTOR, '.pricebar > button')
        self.get_text_item = (By.CSS_SELECTOR, '.btn_inventory')

    def open_menu(self):
        self.driver.find_element(*self.btn_menu).click()
    
    def view_all_items(self):
        self.open_menu().click()
        self.driver.find_element(*self.a_all_items).click()

    def reset_app(self):
        self.open_menu().click()
        self.driver.find_element(*self.a_reset_app).click()

    def get_text(self, item):
        my_text = self.driver.find_elements(*self.get_text_item)
        return my_text[item].text


    def add_new_item_to_cart(self, item):
        my_item = self.driver.find_elements(*self.find_item)
        my_item[item].click()

    def ordery_by_attribute(self, value):
        select = Select(self.driver.find_element(*self.select_product_sort_container))
        select.select_by_value(value)

    def log_out(self):
        self.open_menu()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.a_logout).click()
    
