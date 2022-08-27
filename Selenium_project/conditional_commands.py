from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:\drivers\chromedriver.exe")
driver.get\
    ("http://newtours.demoaut.com/")

time.sleep(5)

user = driver.find_element_by_name(name="userName")
assert user.is_displayed(), True
assert user.is_enabled(), True

password = driver.find_element_by_name(name="password")
assert password.is_displayed(), True
assert password.is_enabled(), True


user.send_keys("rajarshi.mitra21@gmail.com")
password.send_keys("INDRAJAY")

time.sleep(5)

login = driver.find_element_by_name(name="login")
print(login)

login.click()

# verify the radio buttons

round_trip = driver.find_element_by_css_selector("input[value=roundtrip]")
assert round_trip.is_enabled(), True
print("Round trip is enabled")

print(driver.find_element_by_css_selector("input[value=oneway]").is_enabled())

driver.close()







