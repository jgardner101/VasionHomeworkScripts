# Test to Verify login failed with an incorrect Username

from selenium import webdriver
import time

username = "jgrdner"
password = "TestAutomation20211!"

url = "https://joshgardner.printercloud.com/admin/"

driver = webdriver.Chrome("C:/Program Files (x86)\chromedriver.exe")

driver.get(url)

driver.find_element_by_id("relogin_user").send_keys(username)

driver.find_element_by_id("relogin_password").send_keys(password)

driver.find_element_by_id("admin-login-btn").click()

# Validate that user received notification of username or password error

time.sleep(2)
element = driver.find_element_by_id("logintext")
if element.is_displayed():
    print ("Test Succeeded")
else:
    print ("Test Failed")
