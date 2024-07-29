#! python3
# Logging Levels

import logging

logging.basicConfig(level=logging.INFO
, format=' %(asctime)s - %(levelname)s -  %(message)s')
# as long as .INFO is passed to level = 
# only the INFO messages (and the upper categories will be displayed)

logging.debug('Some debugging datails.')

logging.info('The logging module is working')

logging.warning('An error message is about to be logged.')

logging.error('An error has occured.')

logging.critical('The program is unable to recover!')