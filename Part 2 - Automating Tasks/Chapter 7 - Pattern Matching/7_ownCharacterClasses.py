#! python3
# Making our own character classes

import re 

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowels = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(vowels)

consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonants = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(consonants)

lowercasesRegex = re.compile(r'[a-z]')
lowers = lowercasesRegex.findall('PANkesito Rex, omgWAO')
print(lowers)

uppercasesRegex = re.compile(r'[^a-z]')
uppers = uppercasesRegex.findall('PANkesito Rex, omgWAO')
print(uppers)

print() # -----------------------------------

evenRegex = re.compile(r'\d*[02468]')
evens = evenRegex.findall('10, 15, 21, 4, 50, 88, 99, 100, 11, 12, 52, 74, 0, 77, 10006')
print(evens)

oddRegex = re.compile(r'\d*[13579]')
odds = oddRegex.findall('10, 15, 21, 4, 50, 88, 99, 100, 11, 12, 52, 74, 0, 77, 10006, 1, 11, 66, 55, 424109')
print(odds)