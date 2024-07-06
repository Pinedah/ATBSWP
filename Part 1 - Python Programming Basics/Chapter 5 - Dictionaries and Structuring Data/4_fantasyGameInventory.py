
"""
     Write a function named displayInventory() that would take any possible “inventory” and display it like the following:
    Inventory:
    12 arrow
    42 gold coin
    1 rope
    6 torch
    1 dagger
    Total number of items: 62
"""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    totalItems = 0
    print('\nInventory:')
    for key, value in inventory.items():
        print(str(value) + '\t' +  str(key))
        totalItems += int(value)
    print('Total items:\t' + str(totalItems))

displayInventory(stuff)