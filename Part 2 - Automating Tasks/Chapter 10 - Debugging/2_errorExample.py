#! python3
# Getting the Traceback as a String

import traceback

def spam():
    bacon()

def bacon():
    raise Exception('this is the error message, bruh.')

spam()