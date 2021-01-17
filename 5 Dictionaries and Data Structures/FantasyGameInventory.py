# Chapter 5
# Project: List to Dictionary Function for Fantasy Game Inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Display inventory


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(k, v)
    print("\nTotal number of items: " + str(item_total))

# Add item to inventory


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if(item in inventory):
            inventory[item] += 1
        else:
            inventory[item] = 1


# display before
displayInventory(stuff)
# Adding 5 items
addToInventory(stuff, dragonLoot)
# display after
displayInventory(stuff)
