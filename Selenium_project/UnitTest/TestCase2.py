import unittest
import time
from selenium import webdriver


class SearchEngines(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        time.sleep(10)
        print("Title of the page: " + self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        time.sleep(10)
        print("Title of the page: " + self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
