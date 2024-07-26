#! python3
# Program that fill the gaps renaming files 

import os, shutil, pprint, re

dir = "faxinaar"

prefixRegex = re.compile(r'^(faxi)(.*?)?(\d{3})(.*?)?(.)(.*?)')

files = {}
for file in os.listdir(dir):
    if prefixRegex.match(file):
        files[file] = prefixRegex.match(file).group(3)

pprint.pprint(files)

min = int(list(files.values())[0])
for filenumber in files.values():
    if int(filenumber) < min:
        min = int(filenumber)
print('min:', min)

sortedFiles = {}

filenumbers = []
for filenumber in files.values():
    filenumbers.append(int(filenumber))
filenumbers.sort()
print(filenumbers)

newValues = {}
for number in filenumbers:
    newValues[number] = min
    min += 1
pprint.pprint(newValues)

for k, v in files.items():
    if int(v) in list(newValues.keys()):
        files[k] = str(newValues[int(v)]).zfill(3)

pprint.pprint(files)

# rename files
for f in files.keys():
    shutil.copy()

"""

for v in files.values():
    if int(v) == 


for i in range(len(filenumbers)):
    # print(i)
    filenumbers[i] = i + 1
print(filenumbers)


"""