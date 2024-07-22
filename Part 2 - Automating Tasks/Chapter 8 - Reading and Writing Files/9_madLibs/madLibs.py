#! python3 
# madLibs.py - Lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB or VERB  appears in a text file.

madInput = open('input.txt', 'r')
madOutput = open('output.txt', 'w')

phrase = madInput.read()
words = phrase.split()

if not('ADJECTIVE' in words or 'NOUN' in words or 'ADVERB' in words or 'VERB' in words):
    print("There is no such words in input")
else:
    words[words.index('ADJECTIVE')] = str(input('Enter an adjective:'))
    words[words.index('NOUN')] = str(input('Enter a noun:'))
    words[words.index('ADVERB')] = str(input('Enter an adverb:'))
    words[words.index('VERB')] = str(input('Enter a verb:'))

    newPhrase = ' '.join(words)
    print('\nThe bew phrase is:\n' + newPhrase)
    madOutput.write(newPhrase)

