from selenium.webdriver.common.by import By

class PromotionPage():

    def __init__(self, driver):
        self.driver = driver

    _email_field = 'input[name="email"]'
    _password_field = 'input[name="password"]'
    _first_name_field = 'input[name="firstName"]'
    _last_name_field = 'input[name="lastName"]'
    _phone_field = 'input[name="phone"]'


    def get_email_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._email_field)

    def get_password_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._password_field)

    def get_first_name_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._first_name_field)

    def get_last_name_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._last_name_field)

    def get_phone_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._phone_field)

    ''' actions with web elements '''

    def input_email(self, email):
        self.get_email_field().send_keys(email)

    def input_password(self, password):
        self.get_password_field().send_keys(password)

    def input_first_name(self, first_name):
        self.get_first_name_field().send_keys(first_name)

    def input_last_name(self, last_name):
        self.get_last_name_field().send_keys(last_name)

    def input_phone(self, phone_number):
        self.get_phone_field().send_keys(phone_number)

    def complete_promotion_form(self, email, password, first_name, last_name, phone_number):
        self.input_email(email)
        self.input_password(password)
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_phone(phone_number)
