

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for key, value in itemsDict.items():
        print(key.ljust(leftWidth, '.') + str(value).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

print()
printPicnic(picnicItems, 12, 5)
print()
printPicnic(picnicItems, 20, 5)
