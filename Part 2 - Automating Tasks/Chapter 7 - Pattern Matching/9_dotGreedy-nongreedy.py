#! python3
# Matching with dot character (greedy and nongreedy)

import re

nongreedyRegex = re.compile(r'<.*?>')
mo1 = nongreedyRegex.search('<To serve man> for dinner>')
print(mo1.group())
# mo1 its nongreedy, so it will search for the shortest string

greedyRegex = re.compile(r'<.*>')
mo2 = greedyRegex.search('<To serve man> for dinner.>')
print(mo2.group())
# mo2 its greedy, so it will search for the longest string