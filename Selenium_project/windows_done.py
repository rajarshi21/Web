from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.blabbermouth.net/")

driver.find_element_by_xpath("/html/body/div[2]/header/div/nav/ul/li[11]/a").click()

# Get the window handles
print("Current window handle: ", driver.current_window_handle)

# Get all the window handles
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    print(handle)

driver.quit()
