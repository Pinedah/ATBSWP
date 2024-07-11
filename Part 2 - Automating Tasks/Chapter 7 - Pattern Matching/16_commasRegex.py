#! python3
# Match a number when this is separed by commas every 3 digits

import re, pprint


numRegex = re.compile(r'^\d{1,3}(,\d{3})*$') # when using start (^) and end ($) characters, search() matches the first and last char, it need to be passed just a single string

test = ['42', '1,234', '6,232,123', '12,34,121', '1234', '123,456,789,123,', '11', '1,000', '11,000', '1,2,3,4', '111,111', '0', '341,231,312']
matches = []

print()
for t in test:
    if numRegex.search(t):
        matches.append(t)
    else:
        print(t + ' nadota')

pprint.pprint(matches)