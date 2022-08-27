from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:\drivers\chromedriver.exe")
driver.get("https://www.hardrockavenue.com/")
print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("/html/body/div/header/div/div/div[2]/div/ul/li[2]/a/b").click()

time.sleep(10)

driver.close() # This will close the parent tab
# #driver.quit() will close all the tabs
