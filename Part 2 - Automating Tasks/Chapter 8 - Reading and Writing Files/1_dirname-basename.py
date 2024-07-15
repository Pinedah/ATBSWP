#! python3
# 

import os

path = 'C:\\Windows\\System32\\calc.exe'
#        dirname              || basename

print(os.path.dirname(path)) # 
print(os.path.basename(path)) #
print(os.path.split(path)) # tuple with (dirname, basename)

path_tuple = (os.path.dirname(path), os.path.basename(path))
print(path_tuple) # exactly same tuple that with split

print(path.split(os.path.sep))
print(os.getcwd().split(os.path.sep))