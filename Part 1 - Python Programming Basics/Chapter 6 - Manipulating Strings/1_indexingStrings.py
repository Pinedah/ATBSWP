
# string can be indexed an sliced just like lists

spam_str = 'Hello world!'

print()
print(spam_str[0]) # H
print(spam_str[4]) # o
print(spam_str[-1]) # !
print(spam_str[0:5]) # Hello
print(spam_str[:5]) # Hello 
print(spam_str[6:]) # world!

another_str = spam_str[:7] + spam_str[-1]
print(another_str)
