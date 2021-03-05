# Test to verify successful login with correct username and password

from selenium import webdriver
import time

username = "jgardner"
password = "TestAutomation20211!"

url = "https://joshgardner.printercloud.com/admin/"

driver = webdriver.Chrome("C:/Program Files (x86)\chromedriver.exe")

driver.get(url)

driver.find_element_by_id("relogin_user").send_keys(username)

driver.find_element_by_id("relogin_password").send_keys(password)

driver.find_element_by_id("admin-login-btn").click()

# Validate Login by looking for the "General" tab

time.sleep(2)
element = driver.find_element_by_id("oGeneral")
if element.is_displayed():
    print ("Test Succeeded")
else:
    print ("Test Failed")
