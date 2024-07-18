#! python3 
# Finding Files and Folder Contents

import os, pprint

print()

dirs = os.listdir('C:\\Users\\Dell Latitude\\Documents\\LIBROS')
pprint.pprint(dirs)

totalSize = 0

for file in dirs:
    totalSize += os.path.getsize(os.path.join('C:\\Users\\Dell Latitude\\Documents\\LIBROS', file))

print('\nThe total size in the LIBROS directory is:', str(totalSize))