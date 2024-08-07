#! python3
# Sending an email from the WIN + R

import sys, logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# logging config 
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
# logging.disable(logging.CRITICAL)

# User Credentials
userEmail = 'papanacho.nacho@gmail.com'
userPass = 'Papanacho12345'

browser = webdriver.Chrome()
try:
    browser.get('http://gmail.com')
    
    emailElem = browser.find_element(By.TAG_NAME, 'input')
    emailElem.send_keys(userEmail)
    
    emailButton = browser.find_element(By.TAG_NAME, 'button')
    emailButton.click()

except NoSuchElementException:
    print("\nNope.")