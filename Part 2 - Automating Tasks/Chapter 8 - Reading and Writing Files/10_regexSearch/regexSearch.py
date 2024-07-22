#! python3
# Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen. 

import re, os, pprint

folder = 'C:\\Users\\Dell Latitude\\Documents\\GitHub\\ATBSWP\\Part 2 - Automating Tasks\\Chapter 8 - Reading and Writing Files\\10_regexSearch\\files'

# User enter the regex
input = str(input('Enter your regex: '))
userRegex = re.compile(input)

# Access to every file in a folder
filenames = []
if os.path.exists(folder):
    filenames = os.listdir(folder)
    print(filenames)

# Create file objects
files = []
for name in filenames:
    files.append(open(folder + '\\' + name, 'r'))

# Read files
filesContents = []
for file in files:
    filesContents += file.readlines()
pprint.pprint(filesContents)

# Look for the lines that matches with the regex
matches = []
for line in filesContents:
    if userRegex.search(line):
        matches.append(line)
        
# TODO: Print the results
print('\n' + str(matches))