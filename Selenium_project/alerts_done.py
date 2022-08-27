from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]"
                             "/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]"
                             "/button").click()

time.sleep(5)
driver.switch_to_alert().accept()  # Click OK
time.sleep(5)

driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]"
                             "/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]"
                             "/button").click()
time.sleep(5)
driver.switch_to_alert().dismiss()  # Click Cancel
time.sleep(5)

driver.quit()
