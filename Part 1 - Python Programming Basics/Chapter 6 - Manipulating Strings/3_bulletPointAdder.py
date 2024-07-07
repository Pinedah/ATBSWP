#! python3
# bulletPointAdder.py - Ads Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# separate lines an add stars.
lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes for "lines" list
    lines[i] = '*' + lines[i]   # add star to each string in "lines" list
text = '\n'.join(lines)

pyperclip.copy(text)
print('\nSuccessfully  copied to clipboard!!...\n')