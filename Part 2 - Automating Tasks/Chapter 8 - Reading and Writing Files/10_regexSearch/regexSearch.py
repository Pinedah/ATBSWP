#! python3
# Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen. 

import re, os

# TODO: User enter the regex
input = str(input('Enter your regex: '))
userRegex = re.compile(input)

# TODO: Access to every file in a folder
folder = 'C:\\Users\\Dell Latitude\\Documents\\GitHub\\ATBSWP\\Part 2 - Automating Tasks\\Chapter 8 - Reading and Writing Files\\10_regexSearch\\files'

if os.path.exists(folder):
    files = os.listdir(folder)
    print(files)

# TODO: Read LINES in every file in a folder



# TODO: Look for the lines that matches with the regex

# TODO: Print the results