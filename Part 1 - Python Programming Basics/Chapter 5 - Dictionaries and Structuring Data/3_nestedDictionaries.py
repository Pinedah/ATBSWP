
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item): # takes the dictionary and the item searched
    numBrougth = 0 # initialize a variable for the count (counter)
    for names, values in guests.items(): # names is for keys | values is for values for each name (Alice, Bob, Carol)
        # k is never used, but it lets 'v' be the variable for the seconds items in the dic, those are the values for every name
        numBrougth = numBrougth + values.get(item, 0) # if get finds the item that is being searched, it will return the number of it, otherwise return 0
    return numBrougth # the function will return the counter
 
print('Number of things being brought')
print(' - Apples\t\t' + str(totalBrought(allGuests, 'apples')))
print(' - Cups\t\t\t' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes\t\t' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches\t' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies\t\t' + str(totalBrought(allGuests, 'apple pies')))
