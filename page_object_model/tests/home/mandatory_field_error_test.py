import unittest

from page_object_model.pages.home.home_page import HomePage
from page_object_model.tests.home.base_test import BaseTest
import time


class MandatoryFieldErrorTest(BaseTest, unittest.TestCase):

    def test_mandatory_field_error(self):

        home_page = HomePage(self.driver)
        login_page = home_page.click_promo_button()

        login_page.click_email_field()
        login_page.click_password_field()
        time.sleep(2)



if __name__ == "__main__":
    unittest.main()