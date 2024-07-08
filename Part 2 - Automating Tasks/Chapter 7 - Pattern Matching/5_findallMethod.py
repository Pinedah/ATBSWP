#! python3
# The findall() Method

import re
print()

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}') # has no groups
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())

fa = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(fa)

# ----------------------------------------------------
print()

phoneNumRegexG = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # has groups
moG = phoneNumRegexG.search('Cell: 415-555-9999 Work: 212-555-0000')
print(moG.group())
print(moG.group(1))
print(moG.group(2))
print(moG.group(3))

faG = phoneNumRegexG.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(faG)



