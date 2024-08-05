#! python3
# Getting Data from an Element's Attributes

import bs4

soup = bs4.BeautifulSoup(open('example.html'), features='html.parser')

spanElement = soup.select('span')[0]

print()
print(str(spanElement))
print(spanElement.get('id'))
print(spanElement.get('webo'))
print(spanElement.get('some_nonexistent_addr') == None)
print(spanElement.attrs)

print()

