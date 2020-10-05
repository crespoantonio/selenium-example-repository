from selenium.webdriver.common.by import By
from selenium import webdriver

class PageLogIn():
    def __init__(self, driver):
        self.driver = driver
        self.user_name = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.log_in_buttom = (By.CSS_SELECTOR, 'input.btn_action')
        self.error_message = (By.XPATH, '//*[@id="login_button_container"]/div/form/h3')

    def log_in(self, userName, password):
        self.driver.find_element(*self.user_name).clear()
        self.driver.find_element(*self.user_name).send_keys(userName)
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.log_in_buttom).click()