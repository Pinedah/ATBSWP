
# terminate the program when we want with a function

import sys

while True:
    print('\nType "exit" to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('you typed "' + response + '", tonto')