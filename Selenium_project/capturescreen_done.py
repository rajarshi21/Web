from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.delete_all_cookies()

driver.get("https://www.amazon.in/")

driver.save_screenshot("D:\\Selenium_project\\amazon.jpg")

driver.get_screenshot_as_file("D:\\Selenium_project\\amazon.png")
