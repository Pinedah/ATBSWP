#! python3
# 4_renameDates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""
    ^(.*?)              # all text before date
    ((0|1?\d))          # one or two digits for the month
    ((0|1|2|3)?\d)-     # one or two digits for the day
    ((19|20)\d\d)       # four digits for the year
    (.*?)$              # all text after date
""", re.VERBOSE)

# Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(4)
    afterPart = mo.group(5)

# Form the European-style filename.
euroFilename = beforePart + dayPart + '-' + monthPart + '=' + yearPart + afterPart

# Get the full, absolute file paths.
absWorkinDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkinDir, amerFilename)
euroFilename = os.path.join(absWorkinDir, euroFilename)

# Rename the files.
print(f'Renaming {amerFilename} to {euroFilename}')

# shutil.move(amerFilename, euroFilename) 
