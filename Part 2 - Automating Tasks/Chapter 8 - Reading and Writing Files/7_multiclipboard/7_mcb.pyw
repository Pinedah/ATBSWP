#! python3 
# 7_mcb.pyw - Saves and loads pieces of text to the clipboard

"""
    Usage:  py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
            py.exe mcb.pyw <keyword> - Load keyword to clipboard.
            py.exe mcb.pyw list - Loads all keyword to clipboard.
"""

import shelve, pyperclip, sys


print(sys.argv)
print(len(sys.argv))
print(sys.argv[1])

mcbShelf = shelve.open('mcb')


# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print('si')
elif len(sys.argv) == 2:    
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(mcbShelf.keys()))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
 
mcbShelf.close()