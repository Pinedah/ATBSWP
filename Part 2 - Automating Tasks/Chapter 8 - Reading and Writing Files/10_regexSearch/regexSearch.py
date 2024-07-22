#! python3
# Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen. 

import re, os, pprint

# TODO: User enter the regex
input = str(input('Enter your regex: '))
userRegex = re.compile(input)

# TODO: Access to every file in a folder
folder = 'C:\\Users\\Dell Latitude\\Documents\\GitHub\\ATBSWP\\Part 2 - Automating Tasks\\Chapter 8 - Reading and Writing Files\\10_regexSearch\\files'

filenames = []
if os.path.exists(folder):
    filenames = os.listdir(folder)
    print(filenames)

# TODO: Create file objects
files = []
for name in filenames:
    files.append(open(folder + '\\' + name, 'r'))

# TODO: Read files
filesContents = []
for file in files:
    filesContents.append(file.readlines())
pprint.pprint(filesContents)

# TODO: Look for the lines that matches with the regex


# TODO: Print the results