# Better run this as a separate project.

import unittest
import HtmlTestRunner
from selenium import webdriver
from POMBased_Unittest.PageObjects.login import LoginPage
import time
import sys
sys.path.append("D://Selenium_project//POMBased_Unittest")


class LoginTest(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_login(self):
        login = LoginPage(self.driver)
        login.setusername(self.username)
        login.setpassword(self.password)
        login.click_login()
        time.sleep(5)
        self.assertEqual(self.driver.title, "Dashboard / nopCommerce administration")


if __name__ == "main":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\Reports"))
