from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


import time


fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/jpeg")
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "D:\\")
fp.set_preference("pdfjs.disabled", True)

# chromeOptions.add_experimental_option("prefs", {"download.default_directory":
#                                                 "D:\\"})

driver = webdriver.Firefox(executable_path="C:\\drivers\\geckodriver.exe", firefox_profile=fp)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://pinetools.com/rotate-image")
time.sleep(5)

browse = driver.find_element_by_id("5dc98f708141e-input")
browse.send_keys("D://index.jpg")

time.sleep(15)
# Now in the webpage submit the image, as it is now loaded.


driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/span[1]").click()

time.sleep(10)

# # now do an explicit wait.
# # Explicit wait - start
wait = WebDriverWait(driver, 20)
ele = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='5dc98f7081442']/div[1]/div/button[2]")))
ele.click()


time.sleep(5)

#driver.close()










