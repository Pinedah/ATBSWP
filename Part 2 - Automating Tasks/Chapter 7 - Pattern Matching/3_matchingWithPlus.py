#! python3
# Matching One or More with the Plus

import re

batRegex = re.compile(r'Bat(wo)+man')

mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
print(mo1.group(1))

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
print(mo2.group(1))

mo3 = batRegex.search('The Adventures of Batman')
print(mo3) # None -> cause group (wo) is not even a single time in the search