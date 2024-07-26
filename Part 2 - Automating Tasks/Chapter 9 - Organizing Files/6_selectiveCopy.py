#! python3

"""
Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
"""
print()

import os, pprint, shutil, re

dir = 'selectiveCopy' # directory where to search
extensionsRegex = re.compile(r'(.*?)((.)(txt|py|c))$') # put the searched extensions here

# Create new folder
newDir = 'justSelectives'
if not os.path.exists(newDir):
    os.makedirs(newDir)

toMove = []

# Walk into the directory
pprint.pprint(list(os.walk(dir)))
print()

for folderName, subfolders, filenames in os.walk(dir):
    for filename in filenames:
        if extensionsRegex.match(filename):
            toMove.append(os.path.join(folderName, filename))
            print(f'{filename} -', end='')
print()

# Move into the new foler
pprint.pprint(toMove)
print()
for file in toMove:
    shutil.copy(file, newDir)
    print(f'{file} copied to {newDir}')
