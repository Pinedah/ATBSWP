#! python3 
# matching regex objects

import re

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# mo = Match Object
mo = phoneNumRegex.search('My number is 415-555-1242')
if mo != None:
    print('\nPhone number found: ' + mo.group())
else:
    print('No coincidences')