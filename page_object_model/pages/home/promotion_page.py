from selenium.webdriver.common.by import By

class PromotionPage():

    def __init__(self, driver):
        self.driver = driver

    _email_field = 'input[name="email"]'
    _password_field = 'input[name="password"]'
    _first_name_field = 'input[name="firstName"]'

    def get_email_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._email_field)

    def get_password_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._password_field)

    def get_first_name_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._first_name_field)

    ''' actions with web elements '''

    def input_email(self, email):
        self.get_email_field().send_keys(email)

    def input_password(self, password):
        self.get_password_field().send_keys(password)

    def input_first_name(self, first_name):
        self.get_first_name_field().send_keys(first_name)
