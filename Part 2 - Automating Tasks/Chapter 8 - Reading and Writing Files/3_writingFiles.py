#! python3
# Writing to Files

"""
    if you open the file with 'r' 
        you coulnd't write in it
    if you open the file with 'w'
        you will write, if the file has already content, it will be deleted
    if you open the file with 'a' (append)
        you will write, if the file has already content, it will keep the content and write at the end 
"""

baconFile = open('.\\3_files\\bacon.txt', 'w')
