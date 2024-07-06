
#  The in and not in operators can be used with strings just like with list values. 

print('Hello' in 'Hello World') # True
print('Hello' in 'Hello') # True
print('' in 'Hello World') # True
print('cats' not in 'cats and dogs') # False
print(' ' in 'cats and dogs') # True

print('\n\nthe empty string ('') is considered to be a substring of every single string')
print('' in '') # True
print('' in ' ') # True
print('' in 'a') # True
print('' in '33') # True
