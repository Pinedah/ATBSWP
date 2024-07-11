#! python3

import re, pprint

regex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)

fa = regex.findall('''
it must match the following:
•   'Alice eats apples.'
•	'Bob pets cats.'
•	'Carol throws baseballs.'
•	'Alice throws Apples.'
•	'BOB EATS CATS.'
but not the following:
•	'RoboCop eats apples.'
•	'ALICE THROWS FOOTBALLS.'
•	'Carol eats 7 cats.'
''')

pprint.pprint(fa)