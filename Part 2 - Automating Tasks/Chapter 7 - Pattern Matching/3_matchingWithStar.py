#! python 
# Matching Zero or More with the Star

import re

batRegex = re.compile(r'Bat(wo)*man')

mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
print(mo1.group(1)) # None -> there is no the group (wo)

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
print(mo2.group(1)) # wo -> there is that coincidence

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
print(mo3.group(1)) # wo -> there is that coincidence
# print(mo3.group(2)) # ERROR -> there is no a second group; yes, the group (wo) appears several times, but it still being the same group

