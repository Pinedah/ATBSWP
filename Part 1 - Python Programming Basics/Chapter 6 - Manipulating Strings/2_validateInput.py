
print()
while True:
    print('\nEnter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('\nSelect a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers')

print(f'\nNice, your user is: \nAge: {age}\nPassword: {password}')
