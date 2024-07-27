#! python3
# Program that fill the gaps renaming files 

import os, shutil, pprint, re

dir = "faxinaar"

# define the regex 
prefixRegex = re.compile(r'^(faxi)(.*?)?(\d{3})(.*?)?(.)(.*?)')

# get the name of all files
files = {}
for file in os.listdir(dir):
    if prefixRegex.match(file):
        files[file] = prefixRegex.match(file).group(3)

# look for the smallets number in the files
min = int(list(files.values())[0])
for filenumber in files.values():
    if int(filenumber) < min:
        min = int(filenumber)

# sort the files that has matched in order to get it down in the filename
filenumbers = []
for filenumber in files.values():
    filenumbers.append(int(filenumber))
filenumbers.sort()

newValues = {}
for number in filenumbers:
    newValues[number] = min
    min += 1

for k, v in files.items():
    if int(v) in list(newValues.keys()):
        files[k] = str(k).replace(v, str(newValues[int(v)]).zfill(3))

# rename files
for file in files:
    shutil.move(os.path.join(dir, file), os.path.join(dir, files[file]))
    print(f'{os.path.join(dir, file)} renamed as: {files[file]}')
