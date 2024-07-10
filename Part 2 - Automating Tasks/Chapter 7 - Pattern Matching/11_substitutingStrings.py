#! python3
# Substituting Strings with the sub() Method

import re 

namesRegex = re.compile(r'Agent \w+')

censoredNames = namesRegex.sub('CENSORED', 'Agent Fati gave the secret documents to Agent Panke')

print('\n' + censoredNames)

agentNamesRegex = re.compile(r'Agent (\w)\w*') # define the first letter of each name as a group (group 1)
anr = agentNamesRegex.sub(r'\1****', 'Agent Faxi told Agent Pankeeeeee that Agent Citla knew Agent Yoyo was a double agent.') # when pass the sub, say replace for the first group (1) and then four stars

print('\n' + anr)


agentNamesRegex2 = re.compile(r'Agent (\w)(\w*)') # in this case we got two groups
anr2 = agentNamesRegex2.sub(r'\2****', 'Agent Faxi told Agent Pankeeeeee that Agent Citla knew Agent Yoyo was a double agent.') # we are (incorrectly) printing the second group (2) to see the diference 

print('\n' + anr2)