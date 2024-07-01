
x = 5
print(f'\nid x:\t\t{id(x)}')
x = 10
print(f'id x overriden: {id(x)}')

eggs = [1,2,3]
print(f'\nid eggs:\t\t{id(eggs)}')
eggs = [4,5,6]
print(f'id eggs overriden:\t{id(x)}')

spam = [1,2,3]
print(f'\nid spam:\t\t\t{id(spam)}')
del spam[2]
del spam[1]
del spam[0]
spam.append(4)
spam.append(5)
spam.append(6)
print(f'id spam modified properly:\t{id(spam)}')
