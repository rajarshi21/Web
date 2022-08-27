from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path = "C:\drivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path = "C:\drivers\geckodriver.exe")
# Similarly for IE driver

driver.get("https://www.hardrockavenue.com/")

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()
