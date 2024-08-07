#! python3
# Managing Complex Regexes 

import re
import pprint

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

nicerPhoneRegex = re.compile(r'''
    (\d{3}|\(\d{3}\))               # area code -> 123|
    (\s|-|\.)?                      # separator -> _|-|\. 
    \d{3}                           # first 3 digits -> 123
    (\s|-|\.)                       # separator -> _|-|
    \d{4}                           # last 4 digits -> 1234
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension -> _*(ext|x|ext.)\s*12-12345
''', re.VERBOSE)

fa = nicerPhoneRegex.findall('''
Phone number1: 123-123-1234 ext 12345
Phone number2: (123).123 1234 ext.12
Phone number3: (123) 123 1234x12345
Phone number4: 123-123.1234ext. 12
Phone number5: (123) 123 1234 x 123
Phone number6: (123)123.1234
''')

if fa != None:
    pprint.pprint(fa)
else:
    print('nadota')