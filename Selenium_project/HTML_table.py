from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("file:///D:/Selenium_project/sample_table.html")  # Local html file having a table.

rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/td"))

for r in range(1, rows+1):
    for c in range(1, cols+1):
        print(driver.find_element_by_xpath("/html/body/"
                                            "table/tbody/"
                                            "tr["+str(r)+"]/td["+str(c)+"]").text,
              end=' ')
    print()


