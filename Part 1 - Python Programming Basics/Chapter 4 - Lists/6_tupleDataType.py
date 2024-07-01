
# 1. like a list but with ( )
# 2. is immutable 

spamList = ['a', 1, 0,5]
spamTuple = ('f', 1, 0.2)

spamList.append('b')
# spamTuple.append('b') 
# you cannot append, remove or modifie values form tuples 

lilTuple = ('fati',) # if you put a comma after the first element of the tuple, then tehe variable will be a tuple, otherwise, will be just an string
string = ('fati')

print(type(lilTuple))
print(type(string))