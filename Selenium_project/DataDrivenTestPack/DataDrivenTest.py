from DataDrivenTestPack import XLUtil
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://newtours.demoaut.com/")

path = "D:\\Selenium_project\\login.xlsx"

rows = XLUtil.getRowCount(path, 'Sheet1')

for r in range(2, rows+1):
    username = XLUtil.readData(path, r, 1, 'Sheet1')
    password = XLUtil.readData(path, r, 2, 'Sheet1')
    # locate and enter into the ele
    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()

    if driver.title == "Find a Flight: Mercury Tours:":
        print("Pass")
        XLUtil.writeData(path, r, 3, 'Sheet1', "Pass")
    else:
        print("Fail")
        XLUtil.writeData(path, r, 3, 'Sheet1', "Fail")

    driver.find_element_by_link_text("Home").click()

driver.quit()












