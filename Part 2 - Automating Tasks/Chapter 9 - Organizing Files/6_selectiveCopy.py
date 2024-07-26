#! python3

"""
Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
"""

import os, pprint, shutil, re

dir = ''

extensionsRegex = re.compile(r'(.)(txt|py|c)')

# Create new folder
newDir = ''
if not os.path.exists(newDir):
    os.makedirs(newDir)

# Walk into the directory
for folderName, subfolders, filenames in os.walk(dir):
    #print(f'The current folder is {folderName}')
    for subfolder in subfolders:
        #print(f'SUBFOLDER OF {folderName}: {subfolder}')
    for filename in filenames:
        #print(f'FILE INSIDE {folderName}: {filename}')


# Move into the new foler

