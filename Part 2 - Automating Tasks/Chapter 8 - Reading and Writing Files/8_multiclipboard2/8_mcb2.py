#! python3 
# 7_mcb.pyw - Saves and loads pieces of text to the clipboard

"""
    Usage:  py 8_mcb2.py save <keyword>     - Saves clipboard to keyword.
            py 8_mcb2.py <keyword>          - Load keyword to clipboard.
            py 8_mcb2.py list               - Loads all keyword to clipboard.
            py 8_mcb2.py delete <keyword>   - Deletes the keyword given.
            py 8_mcb2.py delete             - Deletes all the keywords.
"""

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
print(list(mcbShelf.keys()))

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save': 
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(sys.argv[2] + ' saved. :)')

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
    print(sys.argv[2] + ' has been deleted.')

elif len(sys.argv) == 2:    
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys()))) # needed to cast to list()

    elif sys.argv[1].lower() == 'delete':
        for keywords in list(mcbShelf.keys()):
            del mcbShelf[keywords]
        print('--all keywords deleted.')

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(sys.argv[1] + ' succesfully copied to clipboard. :)')

    else:
        print("--not in mcbShelf :(")
 
mcbShelf.close()
