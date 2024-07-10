#! python3
# Matching Everything with Dot-Star

import re

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')

mo = nameRegex.search('First Name: Fatima Last Name: Nava')
print(mo.group(1)) # Fatima
print(mo.group(2)) # Nava

mo2 = nameRegex.search('First Name: Whatever 33 Last Name: For Real, whatever lol : saymyname!!')
print(mo2.group(1)) # Whatever 33
print(mo2.group(2)) # For Real, whatever lol : saymyname!!

