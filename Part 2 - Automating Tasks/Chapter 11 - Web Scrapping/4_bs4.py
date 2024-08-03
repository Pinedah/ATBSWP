#! python3
# Using bs4

import bs4

exampleFile = open('example.html')

exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features = "html.parser")

elems = exampleSoup.select('#author')

print()

print("Elems: ")
print(elems)
print("Elems: ", end='')
print(type(elems))
print("Elems: ", end='')
print(len(elems))
print("Elems: ", end='')
print(type(elems[0]))
print("Elems: ", end='')
print(elems[0].getText())
print("Elems: ", end='')
print(str(elems[0]))
print("Elems: ", end='')
print(elems[0].attrs)

print()