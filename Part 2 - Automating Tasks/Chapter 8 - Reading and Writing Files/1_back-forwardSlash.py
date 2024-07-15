#!python3 
# backslash for windows and forward slash for linux

import os

print()
path = os.path.join('usr', 'bin', 'panke')
print(path) # it will add automatically the \
# usr\bin\panke

myFiles = ['accounst.txt', 'details.csv', 'invite.docx']

print()
for filename in myFiles:
    print(os.path.join('C:\\Users\\panke', filename))