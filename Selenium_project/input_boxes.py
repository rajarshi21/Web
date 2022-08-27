from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://volunteersignup.org/register")

inputboxes = driver.find_elements(By.CLASS_NAME, 'form-control')

print("Display status: ",driver.find_element(By.ID, "firstname").is_displayed())
print("Enable status: ", driver.find_element(By.ID, "firstname").is_enabled())

driver.find_element(By.ID, "firstname").send_keys("Rajarshi")
driver.find_element(By.ID, "lastname").send_keys("Mitra")

print("No. of text boxes: ", len(inputboxes))

driver.quit()

