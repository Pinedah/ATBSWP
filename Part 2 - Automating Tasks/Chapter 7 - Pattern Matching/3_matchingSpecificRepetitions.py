#! python3
# Matching Specific Repetitions with Curly Brackets

print()
import re

haRegex = re.compile(r'(Ha){3}')

mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2)

# ----------------------------

haRegex2 = re.compile(r'(Ha){1,7}') # occurrences between 1 and 7

mo3 = haRegex2.search('aaaaaa HaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHa')
print(mo3.group())