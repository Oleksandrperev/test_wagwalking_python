from selenium import webdriver
import unittest
import time
from page_object_model.pages.home.home_page import HomePage


class First_test(unittest.TestCase):

    driver_path = '/Users/oleksandr/automation/drivers/chromedriver'
    base_url = 'https://wagwalking.com/'
    expected_title = 'WagWalking.com - Leading Local Dog Walker Service for Dog Owners'

    def test_promotion(self):
        driver = webdriver.Chrome(executable_path=self.driver_path)
        driver.fullscreen_window()
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get(self.base_url)
        actual_title = driver.title
        print(actual_title)
        self.assertEqual(actual_title, self.expected_title, 'actual title is not equal expected title')

        '''
        1-st way to find element
        '''
        # first_walk_free_button = driver.find_element_by_css_selector('p.sc-ifAKCX.yeXEn')

        '''
        2-st way to find element using class By (we should import this class from selenium.webdriver)
        '''

        login_page = HomePage(driver)

        promotion_page = login_page.click_promo_button()

        promotion_page.input_email("alex@gmail.com")

        promotion_page.input_password("1234567a")

        promotion_page.input_first_name('Oleksandr')

        promotion_page.input_last_name('Ivanov')

        #sleep method (sleep 3 sec)
        time.sleep(3)

        driver.quit()


if __name__ == "__main__":
    unittest.main()


