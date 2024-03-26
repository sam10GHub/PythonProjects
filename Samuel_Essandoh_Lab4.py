# Assignment: IT209 – LAB ASSIGNMENT 4 (LA4)
# Purpose:BAGGAGE CONTAINER CLASS DEFINITION
# Name: Samuel Essandoh

class InvItem:
    def __init__(self, item_name):
        self.name = item_name

class Baggage:
    allowed_items = ('pen', 'book', 'coat', 'umbrella', 'gloves', 'jacket', 'food', 'wallet', 'keys', 'laptop', 'phone', 'chapstick', 'spectacles', 'calculator')
    def __init__(self, name, capacity=5):
        self.name = name
        self.capacity = capacity
        self.inventory = []
    def display_items(self):#Displays all items (their names) contained in a Baggage object
        for item in self.inventory:
            print(item.name)

    def add_item(self, item):#Adds an item object to the Baggage object after (1) checking that the max capacity has not been reached (i.e. 5 items) and (2) verifying the item name is in the allowed_items tuple

        if len(self.inventory) < self.capacity:
            if item.name in self.allowed_items:
                self.inventory.append(item)
                return True, item.name + ' Added'
            else:
                return False, 'Item not allowed'
        else:
            return False, 'Reached max capacity'

    def remove_item(self, item):#Removes an item object from the Baggage after checking its presence using check_item method

        if item in self.inventory:
            self.inventory.remove(item)
            return True, item.name +' Removed'
        else:
            return False, 'Item not in inventory'

    def check_item(self, item):#Checks whether an item object is in the Baggage object by using the ‘in’  operator to check presence in the self.inventory lis
        if item in self.inventory:
            return True, 'Item in inventory'
        else:
            return False, 'Item not in inventory'

input('Hit "Enter" to create "backpack1" object with name "My backpack1": \n')
backpack = Baggage('My backpack1')
backpack.display_items()

input('Hit "Enter" to create some "InvItem" objects: \n')
It1 = InvItem("book")
It2 = InvItem("umbrella")
It3 = InvItem("coat")
It4 = InvItem("pen")
It5 = InvItem("cap")
It7 = InvItem("banana")
print('Created for use in this script: ', It1.name, It2.name, It3.name, It4.name,
      It5.name, It7.name)

input('\nT1. Hit "Enter" to add \n\t' + It1.name + '\n\t' + It2.name +
      '\n\t' + It4.name + '\nto ' + backpack.name + '\n')
backpack.add_item(It1)
backpack.add_item(It2)
backpack.add_item(It4)
backpack.add_item(It7)
print(backpack.name, ' now has the following items: ')
backpack.display_items()

input('\nT2. "Enter" to see if ' + backpack.name + ' has ' + It1.name + '  Should see "True" ')
print(backpack.check_item(It1))

input('\nT3. "Enter" to see if ' + backpack.name + ' has ' + It7.name + '  Should see "False" ')
print(backpack.remove_item(It7))

input('\nT4. "Enter" to remove ' + It1.name + ', result: ' + backpack.remove_item(It1)[1])

input('\nT5. "Enter" to add ' + It3.name + ',  result: ' + backpack.add_item(It3)[1])
print('\nShould now have umbrella, pen, and coat in the following list...')
backpack.display_items()

input('\n\nT6. Creating new container with name "My satchel" - add 2 items to container to equal capacity ')
satchel = Baggage('My satchel', capacity=2)
satchel.add_item(It3)
satchel.add_item(It4)
print('\n', satchel.name, ' was created with the following items: ')
satchel.display_items()

input('\nT7. "Enter" to try to add a third item ' + It5.name + ' to force over-capacity condition ')
result, message = satchel.add_item(It5)
print(result, message)

print('\n\nEnd of Lab#4 test script')
