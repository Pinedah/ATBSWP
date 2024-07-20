#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answars in 
# random order, along with the answer key

import random

# The quiz data. Keys are states and values are ther capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files
for quizNum in range(3):
    # TODO: Create the quiz and aswer key files
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answearKeyFile = open('capitalsquiz_answears%s.txt' % (quizNum + 1), 'w')

    # TODO: Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # TODO: Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each
    for questionNum in range(50):

        # Get right and wrong answears
        correctAnswear = capitals[states[questionNum]]
        wrongAnswears = list(capitals.values())
        del wrongAnswears[wrongAnswears.index(correctAnswear)]
        wrongAnswears = random.sample(wrongAnswears, 3)
        answearOptions = wrongAnswears + [correctAnswear]
        random.shuffle(answearOptions)

        # TODO: Write the question and aswear option to the quiz file
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum])) # make the question

        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answearOptions[i])) # pick the letter for the options 
        quizFile.write('\n')

        # TODO: Write the answer key to a file
        answearKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answearOptions.index(correctAnswear)])) # take the correct option for each question 
        # .index("string") -> returns the index where is the correct one

quizFile.close()
answearKeyFile.close()

