
def collatz(number):
    if number % 2 == 0: # number is even
        return number // 2
    else: # number is odd
        return 3 * number + 1
    
print('\nEnter an Natural Number (0 not included)')
while True:
    try:
        num = int(input())
        if num > 0:
            break
    except ValueError:
        print('\nError: Enter an Natural Number')

while num != 1:
    num = collatz(num)
    print(num)

