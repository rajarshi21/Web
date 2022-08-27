from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://www.cleartrip.com/")
ele = Select(driver.find_element_by_id('Adults'))

# different ways for selection.
ele.select_by_visible_text('7')
time.sleep(5)
ele.select_by_index(11)
time.sleep(5)
ele.select_by_value('3')
time.sleep(5)

# count of values
print(len(ele.options), end='')

# print the options

for option in ele.options:
    print(option.text)


