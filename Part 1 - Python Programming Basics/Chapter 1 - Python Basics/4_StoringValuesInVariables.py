
# A variable is like a box in the computer’s memory where you can store a single value. If you want to use the result of an evaluated expression later in your program, you can save it inside a variable.


spam = 40 # the value 40 is in the spam variable
print(f'spam(being an integer) = {spam}')

eggs = 2 # this is called: initializing 

print(spam + eggs) # this is called: use it in expression
print(spam + eggs + spam)

spam = spam + 3 # this is called: overwritting the variable
print(f'spam(being overwritten) = {spam}')

# //////////////////////////////////////////

# then, cause this is py, you can overwrite the variable with a diferent data type (wtf)

spam = 'hello'
print(f'spam(being now a string) = {spam}')

spam = 'wtffffff'
print()
print(f'spam(being overwritten again with another string) = {spam}')

# ////////////////////////////////////////////////
# VARIABLE NAMES

# You can name a variable anything as long as it obeys the following three rules:

# 1. It can be only one word.
# 2. It can use only letters, numbers, and the underscore (_) character.
# 3. It can’t begin with a number

'''
VALID:

balance
currentBalance
current_balance
_spam
SPAM
account4

INVALID:

current-balance
current balance
4account
42
total_$um
'hello'

'''

# VARIABLES ARE CASE SENSITIVE
