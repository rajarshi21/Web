from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("file:///D:/Selenium_project/mouse_hover.html")
time.sleep(10)

# Find the xpath for the DropDown
dropdown = driver.find_element_by_xpath("/html/body/div/button")
blog = driver.find_element_by_xpath("/html/body/div/div/a[1]")

# This is the action object.
action = ActionChains(driver)

action.move_to_element(dropdown).move_to_element(blog).click().perform()

time.sleep(10)

driver.close()



