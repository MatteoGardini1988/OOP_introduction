class Item:
    # class attribute
    pay_rate = 0.8 # The payrate after 20% of discount
    all = [] # List containing all instances of the class


    # Constructor method
    def __init__(self, name: str, price: float, quantity=0.0):
        # Parameters can be assigned to the object DYNAMICALLY since I passed self as an argument
        # quantity has a default value
        # name: we specified the datatype you expect to receive, stringe. And the same holds for price which is a float. Quantity is an integer,
        # since you have specified the default value.

        # Assert is a statement which is used to check a condition. It is useful to validate the argument.
        # You can also add a message to the assertion
        assert price >= 0.0, f"Price {price} is not grater than zero!"
        assert quantity >= 0.0, f"Quantity {quantity} is not grater than zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        # Use the class attribute! This list is filled with the INSTANCES
        Item.all.append(self)







    # define a method: self must be provide. Python pass the object as first argument
    # of the class
    def calculate_total_price(self):
        return self.price * self.quantity

    # Apply a discount

    def apply_discount(self):
        # LOOK that you access to the class attribute by using Item.pay_rate because it is an attribute of the class.
        # Of couse here you can also use self.pay_rate. IF SELF.pay_rate is NOT found then Item.pay_rate is seached for
        self.price = self.price * self.pay_rate

    # If you print the object you do not have a good representation of the object. It would be nicer if you can represent
    # the object in a more user-friendly way.

    def __repr__(self):
        # in order to represent the class uniquely it is a good idea to represent it in the same way we created it
        # NB: '' escapes from ""
        return f"Item('{self.name}',{self.price}, {self.quantity})"


# Instantiate a class: execute automatically the constructor
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)

# This does not cause any error since it is a class attribute! The attribute belongs to the class and NOT to the instance of the class
print(Item.pay_rate)
# FIRST THE ATTRIBUTE IS SEARCHED AT INSTANCE LEVEL AND THE AT CLASS LEVEL
print(item1.pay_rate)

print(Item.__dict__)  # All attributes for CLASS level
print(item1.__dict__)  # All attributes for INSTANCE level

item2.pay_rate = 0.7 # For item2 it finds the attribute at INSTANCE level. It doesn't need to go to CLASS level

item1.apply_discount()
item2.apply_discount()
print(item1.price) # This gives 100*0.8 = 80
print(item2.price) # This gives 1000*0.7 = 700

# How to get all instances of the class? There is not a build in method. You have to use a class attribute
# for instance in Item.all:
#     print(instance.name)

print(Item.all)
# [Item('Phone',80.0, 1), Item('Laptop',700.0, 3), Item('Cable',10, 5), Item('Mouse',50, 5)]
# This is a good practice since you can create instances in the python consolle by simply copy and paste one of this printed
# values.