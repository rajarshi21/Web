from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://newtours.demoaut.com/")

links = driver.find_elements(By.TAG_NAME, "a")
print("No. of links present: ", len(links))

# print the links.
for link in links:
    print(link.text)

driver.find_element(By.LINK_TEXT, "REGISTER").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()



