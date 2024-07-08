#! python3
# grouping matching object with parentheses

import re

# adding parentheses will create groups in the regex 
# (\d\d\d)-(\d\d\d-\d\d\d\d) 
# group(1) - group(2)
# in that case the hyphen is included

phoneNumberRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') # in this case we don't use the hyphen, but a space
mo = phoneNumberRegex.search('My number is (415) 555-4242.')

print()
print(mo.group(1)) # (415)
print(mo.group(2)) # 555-4242

print(mo.group(0)) # (415) 555-4242
print(mo.group()) # (415) 555-4242

print(mo.groups()) # ('(415)', '555-4242')
# multiple-assignment trick to assign each value to separate variables because the mo.groups() returns a Tuple
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)
