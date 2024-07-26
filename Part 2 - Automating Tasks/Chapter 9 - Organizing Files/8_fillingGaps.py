#! python3
# Program that fill the gaps renaming files 

import os, shutil, pprint, re

dir = "faxinaar"

prefixRegex = re.compile(r'^(faxi)(.*?)?(\d{3})(.*?)?(.)(.*?)')

files = {}
for file in os.listdir(dir):
    if prefixRegex.match(file):
        files[file] = prefixRegex.match(file).group(3)

min = int(list(files.values())[0])
for filenumber in files.values():
    if int(filenumber) < min:
        min = int(filenumber)

sortedFiles = {}

filenumbers = []
for filenumber in files.values():
    filenumbers.append(int(filenumber))
filenumbers.sort()

newValues = {}
for number in filenumbers:
    newValues[number] = min
    min += 1

newF = []
for k, v in files.items():
    if int(v) in list(newValues.keys()):
        files[k] = str(k).replace(v, str(newValues[int(v)]).zfill(3))


nFiles = []


# rename files
for file in files:
    shutil.move(os.path.join(dir, file), os.path.join(dir, files[file]))
    print(f'{os.path.join(dir, file)} renamed as: {files[file]}')
