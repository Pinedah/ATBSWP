#! python3
# Saving Variables with the shelve Module

import shelve 

shelfFile = shelve.open('mydata')

# this way you create the shelf, it will create 3 files .bak .dat .dir to store the variable
"""
    shelfFile = shelve.open('mydata')
    cats = ['Zophie', 'Pooka', 'Simon']
    shelfFile['cats'] = cats
    shelfFile.close()
"""

print(type(shelfFile))
print(shelfFile['Cats'])

print(list(shelfFile.keys()))
print(list(shelfFile.values()))

shelfFile.close()