
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: ' + str(divideBy) + ' is an invalid argument')
        return 'srry'

print()

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

def spam2(dividedBy):
    return 42 / dividedBy

print('\nThese ones are with the try clause in the main, not inside the function:')
try:
    print(spam2(2))
    print(spam2(12))
    print(spam2(0))
    print(spam2(1))
except ZeroDivisionError:
    print('Error: Invalid argument and the try block ends here, it wont evaluate the next statement')
    