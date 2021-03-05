# Test to Verify that lost password button triggers a new page with reset option
# Then runs test to enter an invalid email and the send should fail.

from selenium import webdriver
import time

url = "https://joshgardner.printercloud.com/admin/"

driver = webdriver.Chrome("C:/Program Files (x86)\chromedriver.exe")

driver.get(url)

driver.find_element_by_id("forgot-password").click()

print("Please reset your password")


Email = "josh.gardner15gmail.com"

driver.find_element_by_id("email").send_keys(Email)

driver.find_element_by_class_name("ui-button-text").click()

time.sleep(1)
element = driver.find_element_by_xpath("//*[contains(text(),'Please include')]")

if element.is_displayed():
    print ("Test Succeeded")
else:
    print ("Test Failed")
