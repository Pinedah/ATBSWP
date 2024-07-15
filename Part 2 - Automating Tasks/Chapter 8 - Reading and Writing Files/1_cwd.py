#!python3 
# The Current Working Directory

import os

print()
print(os.getcwd())


os.chdir('C:\\Users\\Dell Latitude\\Desktop\\py test')
print()
print(os.getcwd())

os.chdir('C:\\this directory does not exist')
print()
print(os.getcwd())
