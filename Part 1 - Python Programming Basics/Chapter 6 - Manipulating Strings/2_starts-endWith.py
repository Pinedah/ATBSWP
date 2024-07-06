
#  startswith() and endswith() methods return True if the string value they are called on begins or ends (respectively) with the string passed to the method; otherwise, they return False.

print('\n' + str('Hello world!'.startswith('Hello'))) #True
print('Hello world!'.endswith('world!')) # True
print('abc123'.startswith("1")) # False
print('abc123'.endswith("12")) # False

print('Hello world!'.startswith('Hello world!')) # True
print('Hello world!'.endswith('Hello world!')) # True
