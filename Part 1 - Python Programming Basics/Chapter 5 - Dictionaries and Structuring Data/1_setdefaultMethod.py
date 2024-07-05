print()
spam = {'name': 'fati', 'age': 17}

"""
if 'height' not in spam:
    spam['height'] = 1.62
"""

spam.setdefault('height', 1.62)
print(spam.setdefault('height', 1.62))

spam.setdefault('height', 1.70)
print('returns the value in that key:', spam.setdefault('height', 1.70))

print(spam)