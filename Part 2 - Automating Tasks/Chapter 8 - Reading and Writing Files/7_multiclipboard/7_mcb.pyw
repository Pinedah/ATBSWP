#! python3 
# 7_mcb.pyw - Saves and loads pieces of text to the clipboard

"""
    Usage:  py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
            py.exe mcb.pyw <keyword> - Load keyword to clipboard.
            py.exe mcb.pyw list - Loads all keyword to clipboard.
"""

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save': 
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(sys.argv[2] + ' saved. :)')
elif len(sys.argv) == 2:    
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys()))) # needed to cast to list()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print("--not in mcbShelf :(")
 
mcbShelf.close()