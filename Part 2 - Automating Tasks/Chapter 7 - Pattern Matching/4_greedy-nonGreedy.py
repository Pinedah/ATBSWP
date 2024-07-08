#! python3 
# greedy and nongreedy matching

"""
re.compile(r'(Ha){first_limit, second_limit}') # greedy!
re.compile(r'(Ha){first_limit, second_limit}?') # non-greedy!
"""
import re

print()
greedyHaRegex = re.compile(r'(Ha){2,7}')

mo1 = greedyHaRegex.search('why so serious? HaHaHaHaHaHaHaHaHaHaHaHa')
print(mo1.group())


print()
nongreedyHaRegex = re.compile(r'(Ha){2,7}?')

mo2 = nongreedyHaRegex.search('why so serious? HaHaHaHaHaHaHaHaHaHaHaHa')
print(mo2.group())