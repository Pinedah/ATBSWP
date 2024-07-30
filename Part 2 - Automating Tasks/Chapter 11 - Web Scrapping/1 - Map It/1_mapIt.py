#! python3
# 1_mapIt.py - Launches a map in the browser using an address from the command line or clipboard

import webbrowser, sys, logging, pyperclip

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')

logging.info("Starting program... ... ...")
logging.debug(sys.argv)

if len(sys.argv) > 1:
    # Get the address from command line
    address = ' '.join(sys.argv[1:])
    logging.info(address)
else:
    # Get the adress from the clipboard
    address = pyperclip.paste()
    logging.info(address)

webbrowser.open('https://www.google.com/maps/place/' + address)

logging.info("Ending program...\n")