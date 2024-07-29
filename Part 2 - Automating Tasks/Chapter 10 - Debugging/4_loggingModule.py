#! python3
# Using the logging Module

import logging 

# logging.basicConfig(level = logging.DEBUG, format = f'{asctime}s - {levelname}s - {message}s' )
# -> you cant use the fstring format

# its necessary to be: 
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
