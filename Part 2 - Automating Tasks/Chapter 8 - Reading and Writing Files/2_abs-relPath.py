#! python3
# Handling Absolute and Relative Path

import os

print()
print(os.path.abspath('.'))

print()
print(os.path.abspath('.\\Chapter 8 - Reading and Writing Files'))

print()
print(os.path.isabs('.'))

print()
print(os.path.isabs(os.path.abspath('.')))

#-------------------------------

print()
print(os.path.realpath('C:\\Windows'))


print()
print(os.path.realpath('Chapter 8 - Reading and Writing Files'))

print()
print(os.path.realpath('ESCOM'))
