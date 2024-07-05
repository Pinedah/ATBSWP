print()

# using IN and NOT IN operators
spam ={'name': 'fati', 'age': 17}

# if you dont especifie the value, key or item, the operator will evaluate just with KEYS

print('fati' in spam) # fati is not a key, so even when its on the dic, it will return False
print('age' in spam) # age is a key, therefor will return True

print(17 in spam.values())
print('panke' not in spam.values())

print('name' not in spam.keys())

# even works with the items method (WTF)?!!
print(('name', 'fati') in spam.items()) # this shit is true lmao