print()

spam = ['hello', 'hi', 'holi', 'holap']

print(spam.index('hello'))
print(spam.index('holi'))
# print(spam.index('a'))    Value Error

pets = ['dog', 'cat', 'rat', 'fish', 'cat']
print(pets.index('cat')) # cat is duplicate in 1 and 4, python returns the first index

mixed = [101, 'a', 202.0, 'b', 303.7]
print(mixed.index(303.7)) # works with any data type
