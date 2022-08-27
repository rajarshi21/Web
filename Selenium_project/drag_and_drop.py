from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.w3schools.com/html/html5_draganddrop.asp")
time.sleep(5)

source = driver.find_elements_by_xpath("//*[@id='drag1']")
destn = driver.find_elements_by_xpath("//*[@id='div2'']")

actions = ActionChains(driver)
actions.drag_and_drop(source, destn).perform()

time.sleep(5)

driver.close()

# TODO








