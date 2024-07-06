
"""
     Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot.

     The addToInventory() function should return a dictionary that represents the updated inventory. 
"""

def displayInventory(inventory):
    totalItems = 0
    print('\nInventory:')
    for key, value in inventory.items():
        print(str(value) + '\t' +  str(key))
        totalItems += int(value)
    print('Total items:\t' + str(totalItems))

def addToInventory(inventory, addedItems):
    for value in addedItems:
        if value in inventory.keys():
            inventory[value] += 1
        else:
            inventory[value] = 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)