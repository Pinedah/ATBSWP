
import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)

cheese[1] = 42

print('\n' + str(id(spam)))
print(spam)

print('\n' + str(id(cheese)))
print(cheese)