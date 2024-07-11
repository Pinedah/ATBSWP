#! python3
# 14_phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import re, pyperclip, pprint

# phone Regex 
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code [1]
    (\s|-|\.)?                        # separator [2]
    (\d{3})                           # first 3 digits [3]
    (\s|-|\.)                         # separator [4]
    (\d{4})                           # last 4 digits [5]
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension [6] [7] [8]
)''', re.VERBOSE)

# TODO: Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # username
    @                           # @ symbol
    [a-zA-Z0-9.-]+              # domain name
    (\.[a-zA-Z]{2,4})           # dot something
)''', re.VERBOSE)

# TODO: Find matches in the clipboard text
text = str(pyperclip.paste())
matches = []

# printing the data 
pprint.pprint((phoneRegex.findall(text)))
pprint.pprint(emailRegex.findall(text))
#

for groups in phoneRegex.findall(text):
    # group[0] -> the entire phone number
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if(groups[8] != ''):
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
    # final format: 123-123-1234 x12345 or (123)-123-1234 x1234

for groups in emailRegex.findall(text):
    matches.append(groups[0])


# TODO: Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('\nCopied to clipboard:')
    print('\n'.join(matches))
else:
    print('\nNo phone numbers or email addresses found...')

