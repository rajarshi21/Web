from selenium import webdriver
import pytest

# pytest -v -s --html-report.html Pytest/test_pytest_html_reports.py
# better make new project for html report cases
# the below has been done without creation of new project just gto show case
# the technique


class TestHardRockAvenue:
    @pytest.yield_fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homepagetitle(self, setup):
        self.driver.get("https://www.hardrockavenue.com/")
        assert "HARD ROCK AVENUE" == self.driver.title
