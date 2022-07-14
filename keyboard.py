# THIS FILE NEED TO IMPORT Item Class
from item import Item


class Keyboard(Item):
    pay_rate = 0.7 # Overwrite the value in the parent class
    def __init__(self, name: str, price: float, quantity=0):
        # Call to super function to have access to all attributes / methods
        # WE ARE BASICALLY CALL THE CONSTRUCTOR OF PARENTS CLASS. There we used all.appen and  hence also here we append
        # the item to the class.
        super().__init__(
            name, price, quantity
        )





