#! python3
# Checking For Errors

import requests

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
# res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

try:
    res.raise_for_status()
except Exception as exc:
    print(f'\n- - - There was a problem: {exc} - - - ')
    
print("Program end...")