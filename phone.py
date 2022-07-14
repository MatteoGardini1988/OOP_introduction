# THIS FILE NEED TO IMPORT Item Class
from item import Item

class Phone(Item):
    # all = []
    pay_rate = 0.5  # Overwrite the value in the parent class. This is POLYMORPHISM since I have the same name (property attribute)
    # for properties in different classes. Sometimes polymorphism and inheritance goes together.
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        # WE ARE BASICALLY CALL THE CONSTRUCTOR OF PARENTS CLASS. There we used all.appen and  hence also here we append
        # the item to the class.
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones

        # This line is not necessary because we have access to all methods and properties in the parent class, including the
        # property we named "all"
        # Phone.all.append(self)



