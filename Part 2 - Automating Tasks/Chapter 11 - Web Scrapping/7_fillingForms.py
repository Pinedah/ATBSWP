#! python3
# Filling Out and Submitting Forms

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()

try:

    browser.get('http://gmail.com')
    
    emailElem = browser.find_element(By.TAG_NAME, 'input')
    emailElem.send_keys('papanacho.nacho@gmail.com')
    
    emailButton = browser.find_element(By.TAG_NAME, 'button')
    emailButton.click()

except NoSuchElementException:
    print("\nNope.")

# Wait for user input before closing the browser
input("Press Enter to close the browser...")

# Close the browser
browser.quit()
