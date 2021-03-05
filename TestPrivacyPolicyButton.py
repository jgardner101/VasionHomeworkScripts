# Test to Verify That Privacy Policy functions as expected

from selenium import webdriver
import time

url = "https://joshgardner.printercloud.com/admin/"

driver = webdriver.Chrome("C:/Program Files (x86)\chromedriver.exe")

driver.get(url)

link = driver.find_element_by_link_text("Privacy Policy")
link.click()

# Validate that the user reached the privacy policy page
time.sleep(3)

if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[1])
    if driver.current_url.endswith("privacy-policy/"):
        print ("Test Succeeded")
    else:
        print ("Test Failed")

else:
    print("Test Failed")
