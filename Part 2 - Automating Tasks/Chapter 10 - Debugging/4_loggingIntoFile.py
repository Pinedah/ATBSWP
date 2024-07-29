#! python3
# Logging into a file so you don't fill your screen with logging alerts

import logging

logging.basicConfig(filename = 'myProgramLog.txt', level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')

logging.error('This is an error message that displays in the text file')

print('\nThis will display in console')

logging.warning('This is a warning message that displays in the text file')
