#! python3
# Case-Insensitive Matching

import re

robocop = re.compile(r'robocop', re.IGNORECASE)
# also works: re.I

rc1 = robocop.search('RoboCop is part man, part machine, all cop.')
print(rc1.group())

rc2 = robocop.search('ROBOCOP protects the innocent.')
print(rc2.group())

rc3 = robocop.search('Al, why does your programming book talk about robocop so much?')
print(rc3.group())


