import csv


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

        # Double underscore TOTALLY prevents the access from outside the class to your attribute
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        # Use the class attribute! This list is filled with the INSTANCES
        Item.all.append(self)

    @property
    def price(self):
        return self.__price


    @property
    # Property decorator = Read-Only Attribute
    # This is a read only because it a function that returns __name. But you cannot change the name to this
    # function by doing item_class_instances.name=value, because it is a function.
    # name is read only if the method setter is not implemented. Otherwise it is not read only
    def name(self):
        return self.__name

    # I want to set a new value for name althought it is a property with a read only attribute.
    # This time a command like: item_class_instances.name=value works!
    # Define the setter property to the property name you defined. Remember you have to pass a value to set __name
    @name.setter
    def name(self, value):
        # You can also put some other code here: like control of what you are passing.
        if len(value) >= 10:
            raise Exception("The name is to long")
        else:
            # set the new value of __name
            self.__name = value

    # Apply an increment in price
    # THIS IS ENCAPSULATION SINCE WE MODIFY A PROPERTY BY USING A METHOD AND NOT DIRECTLY!
    def apply_increments(self,increment):
        # LOOK that you access to the class attribute by using Item.pay_rate because it is an attribute of the class.
        # Of couse here you can also use self.pay_rate. IF SELF.pay_rate is NOT found then Item.pay_rate is seached for
        self.__price = self.__price + self.__price*increment

    # define a method: self must be provided. Python pass the object as first argument
    # of the class
    def calculate_total_price(self):
        return self.__price * self.quantity
    # Read data from CSV and instantiate. The problem here is that we want to use this method to instantiate a instance.
    # BUT methods are called on instances! So... what can I do? This is why we need a class method. CLASS METHODS DO NOT
    # HAVE A SELF ARGUMENT. IT MUST BE CONVERTED TO CLASS METHOD BY USING A DECORATOR which change the behaviour of the class. When
    # we call a class method the class itself is passed to the method as first argument.
    @classmethod
    def instantiate_from_csv(cls):
        # read the csv file and instanciate
        with open('my_csv.csv','r') as f:
            # Read the whole csv file as a dictionary
            reader = csv.DictReader(f)
            items = list(reader)

        # Instanciate by looping over the list and getting the proper attributes with the function .get.
        for item in items:
            # print(item) # if you want to print
            # remenber to convert to integers
            Item(
                 name=item.get('name'),
                 price=float(item.get('price')),
                 quantity=int(item.get('quantity'))
                 )


    # A static method to check if a number is an integer.
    # A static method receives arguments but not self. It behaves as a normal function
    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero.
        # for i.e: 5.0, 10.0
        # check if a given parameter is an instance of a given class
        if isinstance(num, float):
            # count out the floats that are point zero: namely, if num is 9.0 it counts out the .0 and say: "yes it is am
            # integer: return True"
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    # Apply a discount
    def apply_discount(self):
        # LOOK that you access to the class attribute by using Item.pay_rate because it is an attribute of the class.
        # Of couse here you can also use self.pay_rate. IF SELF.pay_rate is NOT found then Item.pay_rate is seached for
        self.__price = self.__price * self.pay_rate

    # If you print the object you do not have a good representation of the object. It would be nicer if you can represent
    # the object in a more user-friendly way.

    def __repr__(self):
        # in order to represent the class uniquely it is a good idea to represent it in the same way we created it
        # NB: '' escapes from ""
        # return f"Item('{self.name}',{self.price}, {self.quantity})"
        # YOU CAN PRINT THE REAL NAME OF THE CLASS BY calling self.__class__.__name__
        return f"{self.__class__.__name__}('{self.name}',{self.__price}, {self.quantity})"


    # ABSTRACTION: the methods connect, prepare_body and send arec called only from the send_email.
    # We want to remove the access to them from the instance. This is exactly what abstraction is about.
    # This can be done by a double underscore
    def __connect(self,smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} times.
        Regards.
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect("SMTP:connection_server")
        self.__prepare_body()
        self.__send()
