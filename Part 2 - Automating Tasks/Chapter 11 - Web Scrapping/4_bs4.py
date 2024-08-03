#! python3
# Using bs4

import bs4

exampleFile = open('example.html')

exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features = "html.parser")

elems = exampleSoup.select('#author')

print()

print("Elems: ")
print(elems)
print("type: ", end='')
print(type(elems))
print("len: ", end='')
print(len(elems))
print("type(elems[0]): ", end='')
print(type(elems[0]))
print("elems[0].getText(): ", end='')
print(elems[0].getText())
print("str(elems[0]): ", end='')
print(str(elems[0]))
print("elems[0].attrs: ", end='')
print(elems[0].attrs)

print()