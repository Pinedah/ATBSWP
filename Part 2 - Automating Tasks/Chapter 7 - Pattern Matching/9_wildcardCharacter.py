#! python3
# The . (or dot) character in a regular expression is called a wildcart
# . will match any character except for a newline

import re 

atRegex = re.compile(r'.at')
fa = atRegex.findall('The cat in the hat sat on the flat mat')

print(fa)
# cat hat sat lat mat
#           not flat, because the . character just match the first character before 'at'
