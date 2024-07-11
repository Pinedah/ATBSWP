#! python3
# combining re.IGNORACASE re.DOTALL re.VERBOSE

import re

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

some = someRegexValue.findall(r'''
FOO                 # FOO
foO                 # foO
foo                 # foo
FoO                 # FoO                  
''')

print(some)

