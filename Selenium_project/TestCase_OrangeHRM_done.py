from selenium import webdriver
import unittest
import HtmlTestRunner


class HardRockAvenueTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_homepageTitle(self):
        self.driver.get("http://www.hardrockavenue.com/")
        self.assertEqual("[THE HARD ROCK AVENUE]", self.driver.title)

    def test_dosomething(self):
        self.assertTrue(True)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print("Done with all the tests")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D://Selenium_project//Reports"))
