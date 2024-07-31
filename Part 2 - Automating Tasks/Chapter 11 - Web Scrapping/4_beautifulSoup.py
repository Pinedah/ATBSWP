#! python3
# Creating a BeautifulSoup Object from HTML 

import requests, bs4

res = requests.get('http://nostarch.com')

res.raise_for_status() # veifies everything's ok
noStarchSoup = bs4.BeautifulSoup(res.text, features="html.parser") # create the bs4 object 
# features = "html..." specifies the parser library that BeautifulSoup should use to parse the HTML content.
print(type(noStarchSoup)) # print the type

print('-------------------------------------------\n\n')

exampleFile = open('example.html') # also can be opened an local file

exampleSoup = bs4.BeautifulSoup(exampleFile, features="html.parser")
print(type(exampleSoup))