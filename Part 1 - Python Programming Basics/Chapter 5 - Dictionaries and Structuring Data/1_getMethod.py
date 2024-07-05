
# the GET method
# get will take two arguments:
#       get(key_of_the_value, fallback_value)
picnicItems = {'apples': 5, 'cups': 2}

print('\nI am bringing ' + str(picnicItems.get('cups', 0)) + ' cups, and ' + str(picnicItems.get('apples', 'no apples')) + ' apples \n')

print('\nI am bringing ' + str(picnicItems.get('pears', 0)) + ' pears, and ' + str(picnicItems.get('juice', 'no juice')) + '\n')

