#! python3

"""
Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
"""

import os, pprint, shutil, re

dir = ''

extensionsRegex = re.compile(r'(.*?)((.)(txt|py|c))$')

# Create new folder
newDir = 'newD'
if not os.path.exists(newDir):
    os.makedirs(newDir)

toMove = []
# Walk into the directory
for folderName, subfolders, filenames in os.walk(dir):
    #for subfolder in subfolders:
    for filename in filenames:
        if extensionsRegex.match():
            #toMove.append(filename)
            print(f'{filename} appended')


# Move into the new foler

for file in toMove:
    #shutil.copy(file, newDir)
    print(f'{file} copied to {newDir}')
