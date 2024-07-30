#! python3
# 1_mapIt.py - Launches a map in the browser using an address from the command line or clipboard

import webbrowser, sys, logging

if len(sys.argv) > 1:
    # Get the address from command line
    address = ' '.join(sys.argv[1:])

# TODO : Get the adress from the clipboard