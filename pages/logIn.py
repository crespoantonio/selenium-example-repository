from selenium.webdriver.common.by import By

class PageLogIn():
    def __init__(self, myDriver):
        self.driver = myDriver
        self.user_name = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.log_in_buttom = (By.CSS_SELECTOR, 'input.btn_action')

    def log_in(self, userName, password):
        self.driver.find_element(*self.user_name).send_keys(userName)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.log_in_buttom).click()