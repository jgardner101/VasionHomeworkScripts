# Test to Verify login failed with an incorrect password

from selenium import webdriver
import time

username = "jgardner"
password = "TestAutomati"

url = "https://joshgardner.printercloud.com/admin/"

driver = webdriver.Chrome("C:/Program Files (x86)\chromedriver.exe")

driver.get(url)

driver.find_element_by_id("relogin_user").send_keys(username)

driver.find_element_by_id("relogin_password").send_keys(password)

driver.find_element_by_id("admin-login-btn").click()

# Validate password succeeded or failed

time.sleep(2)
element = driver.find_element_by_id("logintext")
if element.is_displayed():
    print ("Test Succeeded")
else:
    print ("Test Failed")
