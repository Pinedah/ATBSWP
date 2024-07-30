#! python3
# Debugging Coint Toss

import random, logging

logging.basicConfig(level=logging.DEBUG
, format=' %(asctime)s - %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)

guess = ''
cases = ('heads', 'tails') # declare a tuple for the cases

while guess not in cases:
    print("\nGuess the coin toss! Enter heads or tails: ")
    guess = input().lower() # make it case insensitive

#toss = random.randint(0, 1) # 0 is tails, 1 is heads 
toss = random.choice(cases) # to make it the random choice in strings

logging.debug(guess)
logging.debug(toss)

if toss == guess:
    print("You got it!")
else:
    print("Nope! Guess again!")
    guess = input().lower() # make it case insensitive

    logging.debug(guess)
    logging.debug(toss)

    if toss == guess:
        print('You got it!')
    else:
        print("Nope. You are really bad at this game xd.")