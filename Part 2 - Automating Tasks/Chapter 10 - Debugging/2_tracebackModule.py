#! python3
# Getting the Traceback as a String

import traceback

try:
    raise Exception('This is the error message, bruh. :D')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt . :D')

    