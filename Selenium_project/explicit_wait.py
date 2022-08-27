from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://www.expedia.com/")

# driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element(By.ID, "tab-flight-tab-hp").click() # Flight button

time.sleep(2)  # from python

driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO") # Source text box
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC") # Destination text box

driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("11/11/2019") # Departure date box
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("12/11/2019") # Departure date box

# Click on search
driver.find_element_by_xpath('/html/body/meso-native-marquee/section/div/div/div[1]/section'
                             '/div/div[2]/div[2]/section[1]/form/div[7]/label/button').click()

# Explicit wait - start
wait = WebDriverWait(driver, 10)  # Explicit wait, it waits for max 10 sec
                                  # for the element to show on the webpage
# wait.driver.find_element(By.ID, "stopFilter_stops-0").click()
ele = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
ele.click()
# Explicit wait - end


time.sleep(3)

driver.quit()
