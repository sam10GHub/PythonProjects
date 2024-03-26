# IT209_LA8- Lab #8
# Name:Samuel Essandoh
#Assignment: Exception Handling



class CartError(Exception):
    pass
class ItemError(Exception):
    def displayErrors(self):
        print('\nItemError exception: ', end ='  ')
        for p in self.args:
            print(p, end= '  ')
        print(' ')

class Shopping:
    allowed_items = ['Pen', 'Books', 'Coat', 'crayon', 'umbrella']

    def __init__(self, name, capacity=5):
        self.name = name
        self.capacity = capacity
        self.inventory = []
        if capacity > 5:
            raise CartError("Cart capacity must be defined as less than or equal to ", 5)

    def add_item(self, itemList):
        """Input: list of items (strings) to be added to the cart (self.inventory)
           Adds each item self.inventory by appending it
           Raises: CartError if len(self.inventory) >= self.capacity, provides an appropriate
                        error message
                   ItemError if an item in itemList is not in allowed_items, provides an
                        appropriate error message
         """
        pass  # 4. replace this line with your code (~7 lines)
        #-------------------------------------------------------
        if len(self.inventory) >= self.capacity:
            raise CartError('Cart already at capacity of: ', self.capacity)
        for item in itemList:
            if item in Shopping.allowed_items:
                self.inventory.append(item)
            else:
                raise ItemError('Item not in the allowed items list: ', item)
    def remove_item(self, item):
        """Input: item (string) to be removed
           Removes the item from the cart (self.inventory)
           Raises: CartError if item is not in the cart (self.inventory) - provides
                   an apprporiate error message.
        """
        pass  # 4. replace this line with your code (~ 6 lines)
        #--------------------------------------------------------
        if item not in self.inventory:
            raise CartError('Item', item, 'is not in ', self.name)
        self.inventory.remove(item)


    def display_items(self):
        """Input:  None/self/void
           Displays the items in the cart (self.inventory)
           Raises CartError with message stating the art is empty.
        """
        # Code is provided with the template - no extra code is needed for this method
        print('\nList of items in ', self.name, ':')
        if len(self.inventory) == 0:
            raise CartError('Cart ' + self.name + ' is empty')
        else:
            for item in self.inventory:
                print(item)


# global code / testscript - no changes are needed to this code, just run it
#--------------------------------------------------------------------------------
print('\n\nTest 1. Hit "Enter" to see Cart1 processed (no errors)')
print('             Add "Pen", "Books" to cart1, then remove "Pen".')
input('-------------------------------------------------------------')

try:
    p1 = Shopping("Cart1")
    p1.add_item(["Pen", "Books"])
    print('Pen, Books added to Cart1')
    p1.display_items()
    p1.remove_item('Pen')
    print('\nPen was removed ')
    p1.display_items()
except Exception as error:
    for m in error.args:
        print(m, end=' ')

print('\n\n\n\nTest 2.  Hit "Enter" to see Cart2 processed. ')
print('    Attempting to define capacity at 7, which is too high. ')
input('-------------------------------------------------------------')
try:
    p2 = Shopping("Cart2", 7)
    print('Tried to create Cart2 with capacity of 7, but max is 5 ')
except CartError as error:
    print('\nCartError exception1: ', end='')
    for m in error.args:
        print(m, end=' ')

print('\n\n\n\nTest 3.  Hit "Enter" to see Cart3 processed.')
print('                    Add "Pen", "Coat", "ball" to Cart3.')
print('                    Exception: "ball" not an allowable item.')
input('-------------------------------------------------------------')
try:
    p3 = Shopping("Cart3", 4)
    p3.add_item(["Pen", "Coat", "ball"])
    print('Trying to add Pen, Coat, and ball to Cart3 - ball not on allowed list')
#except ShoppingError as error:
except ItemError as error:
    error.displayErrors()
finally:
    p3.display_items()

print('\n\n\nTest 4.  Hit "Enter" to see Cart4 processed. ')
print('                 Add "Pen", "Coat" to Cart4, remove "umbrella". ')
print('                 Exception: "umbrella" not in Cart4 ')
input('-------------------------------------------------------------')
try:
    p4 = Shopping("Cart4", 3)
    p4.add_item(["Pen", "Coat"])
    print('Pen, Coat added to Cart4')
    print('\nTrying to remove umbrella from Cart4 - umbrella is not in Cart4 ')
    p4.remove_item('umbrella')
except ItemError as error:
    error.displayErrors()
except CartError as error:
    print('\nCartError exception2: ', end='')
    for m in error.args:
        print(m, end=' ')
finally:
    p4.display_items()

print('\n\n\nTest 5.  Hit "Enter" to see Cart5 processed. ')
print('                 Cart5 capacity is 2, add "Pen", "Coat". ')
print('                 Try to add "crayon": Exception: at capacity. ')
input('-------------------------------------------------------------')

try:
    p5 = Shopping("Cart5", 2)
    p5.add_item(["Pen", "Coat"])
    print('Pen, Coat added to Cart5')
    p5.display_items()
    print('\nTrying to add crayon to Cart5, but already at capacity of 2')
    p5.add_item(['crayon'])
except CartError as error:
    print('\nCartError exception3: ', end='')
    for m in error.args:
        print(m, end=' ')
finally:
    p5.display_items()

print('\n\n\nTest 6.  Hit "Enter" to see Cart6 processed (cart is empty)')
input('-------------------------------------------------------------')
try:
    p6 = Shopping("Cart6", 4)
    print('Trying to display Cart6, which is empty')
    p6.display_items()
except Exception as error:
    print('\nCartError exception4: ', end='')
    for m in error.args:
        print(m, end=' ')

print('\nEnd of Lab #8 Test ')

