# Test to Verify that lost password button triggers a new page with reset option
# Then runs test to select cancel button and exit the password reset page

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = "https://joshgardner.printercloud.com/admin/"

driver = webdriver.Chrome("C:/Program Files (x86)\chromedriver.exe")

driver.get(url)

driver.find_element_by_id("forgot-password").click()

# Test to verify cancel button functions
time.sleep(2)

link = driver.find_element_by_xpath("//*[text() = 'Cancel']")
link.click()

element = driver.find_element_by_id("forgot-password")
if element.is_displayed():
    print ("Test Succeeded")
else:
    print ("Test Failed")
