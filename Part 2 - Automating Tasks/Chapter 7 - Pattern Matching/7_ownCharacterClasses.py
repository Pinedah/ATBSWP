#! python3
# Making our own character classes

import re 

vowelRegex = re.compile(r'[aeiouAEIOU]')

vowels = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(vowels)

consonantRegex = re.compile(r'[^aeiouAEIOU]')

consonants = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(consonants)