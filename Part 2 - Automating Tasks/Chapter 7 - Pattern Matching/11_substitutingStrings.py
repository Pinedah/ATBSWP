#! python3
# Substituting Strings with the sub() Method

import re 

namesRegex = re.compile(r'Agent \w+')

censoredNames = namesRegex.sub('CENSORED', 'Agent Fati gave the secret documents to Agent Panke')

print('\n' + censoredNames)