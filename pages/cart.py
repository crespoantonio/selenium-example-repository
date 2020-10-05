from selenium import webdriver
from selenium.webdriver.common.by import By

class PageCart():
    def __init__(self, driver):
        self.driver = driver
        self.items_on_cart = (By.CSS_SELECTOR, '#cart_contents_container div.cart_item')