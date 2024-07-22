#! python3
# Extracting from ZIP Files

import zipfile, os

exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall() # exctracted in the current dir
exampleZip.extractall('newDir') # creates a new dir named newDir

exampleZip.extract('spam.txt') # will extract just spam.txt file
exampleZip.extract('spam.txt', 'newFolderForSpam') # will extract spam in this new dir


exampleZip.close() 