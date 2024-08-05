#! python3
# Getting Data from an Element's Attributes

import bs4

soup = bs4.BeautifulSoup(open('example.html'), features='html.parser')

print()
print(soup.select('span')) # list
spanElement = soup.select('span')[0]

print(str(spanElement))
print(spanElement.get('id'))
print(spanElement.get('some_nonexistent_addr') == None)
print(spanElement.attrs)
print()

spanElement2 = soup.select('span')[1]
print(spanElement2.attrs)
print(spanElement2.get('class'))

print()

