from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(5)

element = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

# This is the action object.
action = ActionChains(driver)

# For right clicking use the below:
action.context_click(element).perform()

time.sleep(5)

driver.close()



