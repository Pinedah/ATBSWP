#! python3
# Getting Data from an Element's Attributes

import bs4

soup = bs4.BeautifulSoup(open('example.html'), features='html.parser')

print()
print(soup.select('span')) # list

print()
spanElement = soup.select('span')[0]

print(str(spanElement))
print(spanElement.get('id')) # Value in ID
print(spanElement.get('some_nonexistent_addr') == None) # True
print(spanElement.attrs) # dictionary 
print()

spanElement2 = soup.select('span')[1]
print(str(spanElement2))
print(spanElement2.attrs) # dictionary
print(spanElement2.get('class')) # List of classes 
