
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'

print(id(spam))
print(spam)
# [0, 'Hello!', 2, 3, 4, 5]

print(id(cheese))
print(cheese)
# [0, 'Hello!', 2, 3, 4, 5]
