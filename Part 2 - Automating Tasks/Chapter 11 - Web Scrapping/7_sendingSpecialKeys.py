#! python3
# Sending Special Keys

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get('http://nostarch.com')
    htmlElem = browser.find_element(By.TAG_NAME, 'html')
    time.sleep(5)
    htmlElem.send_keys(Keys.END)    # Scrolls to bottom 
    time.sleep(5)
    htmlElem.send_keys(Keys.HOME)    # Scrolls to top
except NoSuchElementException:
    print("\nNope.\n")

time.sleep(5)