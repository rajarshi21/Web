from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.cleartrip.com/")

# To work with checkboxes
# just use the locators to locate the element
# then use isSelected() to see if it is selected or not
# if not, then do a .click() on the found element
# and then verify the status.  same for checkboxes as well.




