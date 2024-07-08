#! python3
# Matching Multiple Groups with the Pipe
# | character is calle a pipe

import re

heroRegex = re.compile(r'Batman|Tina Fey')

mo1 = heroRegex.search('Batman and Tina Fey.')# returns just the first coincidence (Batman)
print(mo1.group()) # Batman

mo2 = heroRegex.search('Tina Fey and Batman') # returns just the first coincidence (Tina Fey)
print(mo2.group()) # Tina Fey

mo3 = heroRegex.findall('Batman and Tina Fey Batman and Tina Fey Batman and Tina Fey') # retuns every coincidence in a list
print(mo3) # print the list

# --------------------------------------------------------
print('\n')

# will find the match one of several patterns as part of the regex
# we can specify the prefix only once and use parentheses and pipe for the other words
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

mo = batRegex.search('Batmobile, and Batbat lost a wheel')

print(mo.group()) # Batmobile
print(mo.group(1)) # mobile
