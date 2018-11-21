# This program adds a given list or dictionary to an inventory
inv = {'rope' : 1, 'torch' : 6, 'gold coin' : 42, 'dagger' : 1, 'arrow' : 12}
dragonLootList = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
dragonLootDict = {'gold coin' : 5, 'sword' : 1, 'jade' : 3}

def displayInventory(inventory):
    """
    Displays the inventory (dictionary) sent by parameter.
    """
    total = 0
    for i, j in inventory.items():
        print('   ' + str(j) + ' ' + i + '(s)')
        total += j
    print('   ' + 'Total: ' + str(total))

def displayLoot(loot):
    """
    Displays the loot (list or dictionary) sent by parameter.
    """
    i = 0
    if type(loot) == list:
        while True:
            print(loot[i], end = '')
            if i == len(loot) - 1:
                print('.')
                break
            elif i == len(loot) - 2:
                print(' and ', end = '')
            else:
                print(', ', end = '')
            i += 1
    if type(loot) == dict:
        keysList = list(loot.keys())
        valuesList = list(loot.values())
        while True:
            print(str(valuesList[i]) + ' ' + keysList[i] + '(s)', end = '')
            if i == len(loot) - 1:
                print('.')
                break
            elif i == len(loot) - 2:
                print(' and ', end = '')
            else:
                print(', ', end = '')
            i += 1

def addListToInv(inventory, items):
    """
    Adds a list of items to the inventory.
    """
    for i in items:
        inventory.setdefault(i, 0)
        inventory[i] += 1

def addDictToInv(inventory, items):
    """
    Adds a dictionay of items to the inventory.
    """
    for i, j in items.items():
        inventory.setdefault(i,0)
        inventory[i] += j

print('Initial inventory:')
displayInventory(inv)

addDictToInv(inv, dragonLootDict)
print('Inventory after dictionary loot: ', end = '')
displayLoot(dragonLootDict)
displayInventory(inv)
print()

addListToInv(inv, dragonLootList)
print('Inventory after list loot: ', end = '')
displayLoot(dragonLootList)
displayInventory(inv)
