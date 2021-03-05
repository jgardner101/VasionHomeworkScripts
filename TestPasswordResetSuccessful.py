# Test to Verify that lost password button triggers a new page with reset option
# Then runs test to enter email and click the reset button to send the email.

from selenium import webdriver
import time

url = "https://joshgardner.printercloud.com/admin/"

driver = webdriver.Chrome("C:/Program Files (x86)\chromedriver.exe")

driver.get(url)

driver.find_element_by_id("forgot-password").click()

print("Please reset your password")

# Test to verify Email entered and submitted for reset

Email = "josh.gardner15@gmail.com"

driver.find_element_by_id("email").send_keys(Email)

driver.find_element_by_class_name("ui-button-text").click()

# Validate that Test email was sent successfully
time.sleep(5)
element = driver.find_element_by_class_name("success")

if element.is_displayed():
    print ("Test Succeeded")
else:
    print ("Test Failed")
