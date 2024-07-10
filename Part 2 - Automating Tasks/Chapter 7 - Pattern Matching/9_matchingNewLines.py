#! python3
# Matching Newlines with the Dot Character 

import re
print()

noNewLineRegex = re.compile(r'.*')
noNL = noNewLineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.')
print(noNL.group()) # Will print just the first line, cause .* does not match the \n

print()

newLineRegex = re.compile('.*', re.DOTALL)
yesNL = newLineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.')
print(yesNL.group()) # will print all

print()
tripleQuotes = newLineRegex.search('''Panke
Faxinaar
Citlaltzin, Yolotzin
Xoloitzcuintle pelon''')
print(tripleQuotes.group())