import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    driver_path = '/Users/oleksandr/automation/drivers/chromedriver'
    base_url = 'https://wagwalking.com/'
    expected_title = 'WagWalking.com - Leading Local Dog Walker Service for Dog Owners'

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.fullscreen_window()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver.get(self.base_url)
        actual_title = self.driver.title
        print(actual_title)
        self.assertEqual(actual_title, self.expected_title, 'actual title is not equal expected title')

    def tearDown(self):
        self.driver.quit()
