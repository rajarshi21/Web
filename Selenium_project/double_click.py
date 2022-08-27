from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://testautomationpractice.blogspot.com/")
time.sleep(10)

element = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/"
                              "div[2]/div[2]/div[2]/"
                              "div/div[4]/div[3]/div/aside/div/div[1]/div[1]/button")

# This is the action object.
action = ActionChains(driver)

#action.double_click(element).perform()
action.context_click(element).perform()

time.sleep(10)

driver.close()



