
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return '\nIt is certain'
    elif answerNumber == 2:
        return '\nIt is decidedly so'
    elif answerNumber == 3:
        return '\nYup'
    elif answerNumber == 4:
        return '\nReply hazy try again'
    elif answerNumber == 5:
        return '\nAsk again later'
    elif answerNumber == 6:
        return '\nConcentrate, bro'
    elif answerNumber == 7:
        return '\nNoup'
    elif answerNumber == 8:
        return '\nLmao'
    elif answerNumber == 9:
        return '\nDoubtful'
    
"""
r = random.randint(1, 9)
fortune = getAswer(r)
print(fortune)
"""    
print(getAnswer(random.randint(1,9)))
