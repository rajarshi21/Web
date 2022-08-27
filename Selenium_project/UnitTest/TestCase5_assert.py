import unittest
import time
from selenium import webdriver


class SearchEngines(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
        self.assertIsNotNone(self.driver)  # Learn about  self.assertIsNone
        self.driver.get("https://www.google.com/")
        time.sleep(10)
        title = self.driver.title

        # assert equal
        self.assertEqual("Google", title, "Title not matched")

        # check for other types of assert.
        # assertNotEqual/assertTrue/assertFalse/assertIsNone/assertIsNotNone
        # assertIn/assertNotIn/assertGreater/assertLess/assertGreaterEqual/assertLessEqual

        self.driver.close()


if __name__ == "__main__":
    unittest.main()
