#! python3
# importing the module re for regular expressions

import re 

phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# this creates the regex object 