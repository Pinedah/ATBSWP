#! python3
# Clicking in the page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Chrome()

browser.get('http://inventwithpython.com')
try:
    linkElem = browser.find_element(By.LINK_TEXT, "The Recursive Book of Recursion")
    print(type(linkElem))
    linkElem.click()
except NoSuchElementException:
    print("Not found!! \n")

# Wait for user input before closing the browser
input("Press Enter to close the browser...")

# Close the browser
browser.quit()