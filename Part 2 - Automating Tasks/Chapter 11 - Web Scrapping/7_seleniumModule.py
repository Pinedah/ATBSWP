#! python3
# Starting a Selenium-Controlled Browser

from selenium import webdriver

browser = webdriver.Firefox() # can select any browser

print(type(browser))
browser.get('http://inventwithpython.com') # opens the page