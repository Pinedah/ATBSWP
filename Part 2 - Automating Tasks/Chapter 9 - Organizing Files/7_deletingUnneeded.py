#! python3
# Write a program that walks through a folder tree and searches for excep tionally large files or folders—say, ones that have a file size of more than 100MB. 

import os, pprint, send2trash

maxSize = 100

# Walk the directory

for folderName, subfolders, filenames in os.walk(dir):
    for filename in filenames:

        # Check file size 
        if os.path.getsize(filename) > maxSize:
            print(f'{filename} is too big, it will be deleted')
            send2trash.send2trash(os.path.join(folderName, filename))
                                  