from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://en.wikipedia.org/wiki/List_of_death_metal_bands,_L%E2%80%93Z")
time.sleep(10)

# Types of scrolls.
# Scroll till some pixel.
# driver.execute_script("window.scrollBy(0,1000)", "")

# Scroll till end of web page
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(10)

# Scroll till an element.
band = driver.find_element_by_link_text("Napalm Death")
driver.execute_script("arguments[0].scrollIntoView();", band)
time.sleep(10)

driver.close()

