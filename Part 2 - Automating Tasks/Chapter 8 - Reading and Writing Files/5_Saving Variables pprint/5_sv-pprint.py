#! python3 
# Saving Variables with the pprint.format() Function

import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'},
        {'name': 'Pooka', 'desc': 'fluffy'}]

pprint.pprint(cats)

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')

fileObj.close()