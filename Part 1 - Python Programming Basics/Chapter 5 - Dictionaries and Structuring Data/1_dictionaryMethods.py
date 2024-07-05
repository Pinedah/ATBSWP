
# values, keys and items

spam = {'name': 'panke', 'age': 19}

print()
print(type(spam.values()))
print(spam.values())
for v in spam.values():
    print(v)

print()
print(type(spam.keys()))
print(spam.keys())
for k in spam.keys():
    print(k)

print()
print(type(spam.items()))
print(spam.items())
for i in spam.items():
    print(i)

print()
for k, v in spam.items():
    print('Key: ' + k + '\t|| Value: ' + str(v))
# k is assigned to the key
# v is assigned to the value