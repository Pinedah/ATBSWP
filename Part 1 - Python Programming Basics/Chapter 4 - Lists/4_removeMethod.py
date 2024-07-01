
# remove(value_in_the_list)

spam = ['cat', 11, 'bat', 11, 'rat', 'elephant', 11]
print(spam)

spam.remove('bat')
print(spam)

spam.remove(11) # as long as this value is repeated in the list, remove() will quit only the first value
print(spam)
