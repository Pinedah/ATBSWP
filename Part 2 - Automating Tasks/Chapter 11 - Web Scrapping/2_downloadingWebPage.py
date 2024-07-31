#! python3 
# Downloading a Web Page with the requests.get() Function

import requests, webbrowser

# webbrowser.open('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

print() # display the type
print(type(res))

print() # check if the status code in the res is OK (200 in https protocol)
print('STATUS CODE FOR OK: ' + str(res.status_code))
print('STATUS CODE FOR OK: ' + str(requests.codes.ok))
print(res.status_code == requests.codes.ok)

print() # len of all the text in the page (number of characters)
print(len(res.text))

print() # displays only the first 250 characters
print(res.text[:250])

