
# This is a guess the number game 

import random

secretNumber = random.randint(1, 20)

print('\nI am thinking of a number between 1 and 20...')

# ask the player to guess 6 times

for guessesTaken in range(1, 7):
    print('\nTake a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break # this means the number is the correct one

if guess == secretNumber:
    print('\nGood job! you guessed my number in:' + str(guessesTaken) + ' guesses!')
else:
    print('\nNope, the number i was thinking of was: ' + str(secretNumber))

