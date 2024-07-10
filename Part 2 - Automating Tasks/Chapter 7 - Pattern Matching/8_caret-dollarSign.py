#! python3 
# The Caret ^ and Dollar Sign $ Characters

import re
print()

beginsWithHello = re.compile(r'^Hello')
bwh = beginsWithHello.search('Hello world!')
print(bwh)
print(bwh.group())

nbwh = beginsWithHello.search('aHello world!')
print(nbwh == None)

string = 'Hello world!'
if string.startswith('Hello'):
    print('\n' + string + '; starts with Hello')

print() # -----------------------------------------------

endsWithNumber = re.compile(r'\d$')

ends = endsWithNumber.search('Your number is 11')
if ends:
    print(ends)
    print(ends.group())
else:
    print('It does not ends with number')

notEnds = endsWithNumber.search('Your number is aa')
if notEnds:
    print(notEnds)
    print(notEnds.group())
else:
    print('It does not ends with number')

print() # -----------------------------------------------

wholeStringIsNum = re.compile(r'^\d+$')

wholeIs = wholeStringIsNum.search('1234567890')
if wholeIs:
    print(wholeIs)
    print(wholeIs.group())
else:
    print('the whole string is not num')

notWholeIs = wholeStringIsNum.search('123a4567890')
if notWholeIs:
    print(notWholeIs)
    print(notWholeIs.group())
else:
    print('the whole string is not num')
