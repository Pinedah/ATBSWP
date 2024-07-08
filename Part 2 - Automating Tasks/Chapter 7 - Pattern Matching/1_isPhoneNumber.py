#! python3
# function that search a pattern for a phone number in a string

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        
    if text[3] != '-':
        return False
    
    for i in range (4, 7):
        if not text[i].isdecimal():
            return False
        
    if text[7] != '-':
        return False
    
    for i in range (8, 12):
        if not text[i].isdecimal():
            return False
    return True

"""
print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))
print('123-123-123a is a phone number:')
print(isPhoneNumber('123-123-123a'))
"""
message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."  

for i in range(len(message)):
    chunk = message[i:i + 12] #  Python’s slicing handles out-of-range indices gracefully by truncating the slice at the end of the string.
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print("done!")

