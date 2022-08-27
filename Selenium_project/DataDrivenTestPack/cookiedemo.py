from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.delete_all_cookies()

driver.get("https://www.amazon.in/")

cookies = driver.get_cookies()
print(len(cookies))  # print no of cookies created.

print(cookies)  # dictionary

# Adding new cookie to the browser.
cookie = {'name': 'MyCookie', 'value': '1234'}
driver.add_cookie(cookie)
print("No of cookies after new addition:")
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))  # print no of cookies created. +1

# We can delete the same cookie as well.
driver.delete_cookie('name')
time.sleep(10)
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))  # count is -1

driver.delete_all_cookies()
print(len(driver.get_cookies()))

driver.quit()







