
#

def eggs(something):
    print('\n' + str(id(something)))
    something.append('hello')

spam = [1, 2, 3]
eggs(spam)

print()
print(id(spam))
print(spam)