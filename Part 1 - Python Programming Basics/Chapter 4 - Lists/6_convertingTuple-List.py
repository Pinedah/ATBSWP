
spamList = ['cat', 'dog', 11]
print(spamList)
print(type(spamList))
print()

spamTuple = tuple(spamList)
print(spamTuple)
print(type(spamTuple))

word = 'faxinaar'
print(f'\nword: {word}, type: {type(word)}')

wordT = tuple(word)
print(f'wordT: {wordT}, type: {type(wordT)}')

wordL = list(word)
print(f'wordL: {wordL}, type: {type(wordL)}')
