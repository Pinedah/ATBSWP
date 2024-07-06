print()
# 

spam = 'Hello world!'
spam = spam.upper()
print(spam)

spam = spam.lower()
print(spam)

print('\n\nfeeling check --------------')
print('How are you?')
feeling = str(input())
if feeling.lower() == 'great':
    print('I feel great too')
else:
    print('I hope the rest of your day is goog.')

print('\n\nisUpper / isLower --------------')

eggs = 'Hello world!'
print(eggs.islower()) # False
print(eggs.isupper()) # False
print('HELLO'.isupper()) # True
print('abc12345'.islower()) # True
print('12345'.islower()) # False
print('12345'.isupper()) # False

