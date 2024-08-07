#! python3
# Finding elements on the page

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
#logging.disable(logging.CRITICAL)

browser = webdriver.Chrome()
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element(By.CLASS_NAME, 'card-img-top')
    print(f"\n\nFound <{elem.tag_name}> element with that class name!\n")
    print(f"\n\nFound <{elem.get_attribute('alt')}> attribute\n!")
except NoSuchElementException:
    print("Was not able to find an element with that class name.")

# Wait for user input before closing the browser
input("Press Enter to close the browser...")

# Close the browser
browser.quit()
