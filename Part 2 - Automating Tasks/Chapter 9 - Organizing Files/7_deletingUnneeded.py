#! python3
# Write a program that walks through a folder tree and searches for excep tionally large files or folders—say, ones that have a file size of more than 100MB. 

import os, pprint, send2trash

maxSize = 5000000
dir = "C:\\Users\\Dell Latitude\\Documents\\LIBROS"
dir2 = "C:\\Users\\Dell Latitude\\Documents\\CECyT 3"


print()
#pprint.pprint(list(os.walk(dir)))


# Walk the directory
for folderName, subfolders, filenames in os.walk(dir2):
    for filename in filenames:
        file = os.path.join(folderName, filename)
        # Check file size 
        if os.path.getsize(os.path.join(folderName, filename)) > maxSize:
            print(f'{filename} is too big, it will be deleted ({os.path.getsize(os.path.join(folderName, filename))})')

            # Send to trash the files that are biggest than the limit
            # send2trash.send2trash(os.path.join(folderName, filename))
                                  