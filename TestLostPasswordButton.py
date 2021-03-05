# Test to Verify that lost password button triggers a new page with reset option

from selenium import webdriver
import time

url = "https://joshgardner.printercloud.com/admin/"

driver = webdriver.Chrome("C:/Program Files (x86)\chromedriver.exe")

driver.get(url)

driver.find_element_by_id("forgot-password").click()

time.sleep(3)

# Validate that the user reached the reset password screen
element = driver.find_element_by_id("email")

if element.is_displayed():
    print ("Test Succeeded")
else:
    print ("Test Failed")
