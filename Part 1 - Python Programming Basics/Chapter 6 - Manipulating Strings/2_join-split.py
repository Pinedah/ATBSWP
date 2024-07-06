
spam = ['cats', 'rats', 'bats']
string = ', '.join(spam)

print()
print(string)
print(' '.join(['My', 'name', 'is', 'Panke']))
print('ABC'.join(['My', 'name', 'is', 'Panke']))

# ------------------------------------------------

print()
print('wtf is a kilometer ?!'.split())
print('MyABCnameABCisABCPankesitoABCRex'.split('ABC'))
print('My name is Pankesito Rex'.split('m'))

# ------------------------------------------------

print()
eggs = ''' Dear Fati,
How have you been? I'm fine.
There is a containter in the fridge
that is labeled "Milk Experiment"

Please do not drink it.
Sincerely,
Panke.'''

print(eggs.split('\n'))