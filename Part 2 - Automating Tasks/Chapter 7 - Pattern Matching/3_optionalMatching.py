#! python3
# Optional Matching with the Question Mark

import re

batRegex = re.compile(r'Bat(wo)?man')

mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

# ---------------------------------------------
print()

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

mo3 = phoneRegex.search('My number is 415-555-4242')
print(mo3.group())

mo4 = phoneRegex.search('My number is 555-4242')
print(mo4.group())