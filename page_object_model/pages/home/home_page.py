from selenium.webdriver.common.by import By
from page_object_model.pages.home.promotion_page import PromotionPage


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    _promo_button = 'p.sc-ifAKCX.yeXEn'

    def get_promo_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._promo_button)

    # actions with web elements
    def click_promo_button(self):
        self.get_promo_button().click()
        return PromotionPage(self.driver)






