#! python3 
# madLibs.py - Lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB or VERB  appears in a text file.

wordsToReplace = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']

madInput = open('input.txt', 'r')
madOutput = open('output.txt', 'w')

madContent = madInput.read() # read the text file
fileWords = madContent.split() # split each word in a list

for madWord in fileWords:
    for repWord in wordsToReplace:
        if repWord in madWord: # look for the coincidence in the strings
            userWord = str(input(f'Enter your {repWord}: ')) # read the users new word
            replacedWord = fileWords[fileWords.index(madWord)].replace(repWord, userWord) # replace it in the specific element of the phrase (this prevents the . ! ? or any other sign)
            fileWords[fileWords.index(madWord)] = replacedWord # put the replacedWord again in the original list of the input

newPhrase = ' '.join(fileWords)
print(newPhrase)
madOutput.write(newPhrase)
