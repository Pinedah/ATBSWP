#! python3
# Strong Password Detection

import re

def is_Strong(password):
    if len(password) < 8:
        return False
    
    hasLower = re.compile(r'[a-z]')
    lower = hasLower.search(password)
    hasUpper = re.compile(r'[A-Z]')
    upper = hasUpper.search(password)
    hasNumber = re.compile(r'[0-9]')
    num = hasNumber.search(password)

    if lower and upper and num:
        return True
    else: 
        return False

while True:
    print("\nEnter your password (empty to break): ")
    password = str(input())
    if password == '':
        break
    if is_Strong(password):
        print("Your password is strong!!")
    else:
        print("Change that shit, dawg!")
