#! python3
# Matching Everything with Dot-Star

import re

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')

mo = nameRegex.search('First Name: Fatima Last Name: Nava')
print(mo.group(1)) # Fatima
print(mo.group(2)) # Nava