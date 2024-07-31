#! python3
# Creating a BeautifulSoup Object from HTML 

import requests, bs4

res = requests.get('http://nostarch.com')

res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, features="html.parser")
print(type(noStarchSoup))

print('-------------------------------------------\n\n')

exampleFile = open('example.html')

exampleSoup = bs4.BeautifulSoup(exampleFile, features="html.parser")
print(type(exampleSoup))