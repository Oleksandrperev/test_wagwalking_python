import unittest
import time
from page_object_model.pages.home.home_page import HomePage
from page_object_model.tests.home.base_test import BaseTest


class PromotionTest(BaseTest, unittest.TestCase):

    def test_promotion(self):

        '''
        1-st way to find element
        '''
        # first_walk_free_button = driver.find_element_by_css_selector('p.sc-ifAKCX.yeXEn')

        '''
        2-st way to find element using class By (we should import this class from selenium.webdriver)
        '''

        login_page = HomePage(self.driver)

        promotion_page = login_page.click_promo_button()

        promotion_page.complete_promotion_form('olex@gmail.com', '1234567a', 'Olex', 'Ivanov', '2222222222')

        #sleep method (sleep 1 sec)
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()


