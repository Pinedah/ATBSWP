#! python3
# 4_renameDates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

import shutil, os, re

dir = 'americanDates'

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""
    ^(.*?)              # all text before date
    ((0|1)?\d)-         # one or two digits for the month
    ((0|1|2|3)?\d)-     # one or two digits for the day
    ((19|20)\d\d)       # four digits for the year
    (.*?)$              # all text after date
""", re.VERBOSE)

print(os.listdir(dir))

# Loop over the files in the working directory
for amerFilename in os.listdir(dir):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo == None:
        continue

    #for i in range(9):
    #    print(mo.group(i))

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    print(euroFilename)

    # Get the full, absolute file paths.
    absWorkinDir = os.path.abspath(dir)
    amerFilename = os.path.join(absWorkinDir, amerFilename)
    euroFilename = os.path.join(absWorkinDir, euroFilename)

    # Rename the files.
    # print(f'Renaming {amerFilename} to {euroFilename}')

    shutil.move(amerFilename, euroFilename) 
