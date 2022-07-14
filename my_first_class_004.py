# THIS FILE NEED TO IMPORT Item Class
from item import Item
# from phone import Phone
from keyboard import Keyboard


# The following is no a good practice since it changes the property "name" directly from the code.
item1 = Item("MyItem", 750)

item1.name = "mySItem"

print(item1.name)

item1.apply_increments(0.2)

print(item1.price)


item2 = Keyboard("jjjj",1000,3)
item2.apply_discount()