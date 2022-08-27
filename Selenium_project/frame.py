from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://selenium.dev/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame")  # enter a frame
time.sleep(5)
driver.find_element_by_link_text("org.openqa.selenium").click()  # select ele in the frame
time.sleep(5)
driver.switch_to.default_content()  # come out of the frame
time.sleep(5)

# In this way continue for the remaining frames.

driver.quit()




