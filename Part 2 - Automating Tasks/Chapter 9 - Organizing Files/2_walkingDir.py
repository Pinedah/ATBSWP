#! python3
# Walking a Directory Tree

import os, pprint

dir = '2_delicious'

pprint.pprint(list(os.walk(dir)))
print()

for folderName, subfolders, filenames in os.walk(dir):
    print(f'The current folder is {folderName}')
    for subfolder in subfolders:
        print(f'SUBFOLDER OF {folderName}: {subfolder}')
    for filename in filenames:
        print(f'FILE INSIDE {folderName}: {filename}')
    
    print('\n')