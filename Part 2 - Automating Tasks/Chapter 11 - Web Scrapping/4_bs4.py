#! python3
# Using bs4

import bs4

exampleFile = open('example.html')

exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features = "html.parser")

elems = exampleSoup.select('#author')

print()

print("Elems: ")
print(elems)
print("Elems: ")
print(type(elems))
print("Elems: ")
print(len(elems))
print("Elems: ")
print(type(elems[0]))
print("Elems: ")
print(elems[0].getText())
print("Elems: ")
print(str(elems[0]))
print("Elems: ")
print(elems[0].attrs)

print()