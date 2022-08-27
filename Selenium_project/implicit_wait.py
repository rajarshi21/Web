from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:\drivers\chromedriver.exe")
driver.get\
    ("http://newtours.demoaut.com/")
assert "Welcome: Mercury Tours" in driver.title

driver.implicitly_wait(10) # This needs to be declared once after the page
                           # get() has been called, so that it is applicable
                           # for all the elements.
user = driver.find_element_by_name(name="userName").send_keys("rajarshi.mitra21@gmail.com")

password = driver.find_element_by_name(name="password").send_keys("INDRAJAY")


login = driver.find_element_by_name(name="login").click()


# verify the radio buttons

round_trip = driver.find_element_by_css_selector("input[value=roundtrip]")
assert round_trip.is_enabled(), True
print("Round trip is enabled")

print(driver.find_element_by_css_selector("input[value=oneway]").is_enabled())

driver.close()







