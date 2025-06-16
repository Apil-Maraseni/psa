# This code demonstrates the creation of a class in Python, instantiation of an object, and calling a method to print attributes.

# create the class
class Bicycle:
    def __init__(self, gear, speed):
        # initialize attributes
        self.gear = gear
        self.speed =speed
    
    # create the print_attributes() method 
    def print_attributes(self):
        print(self.gear)
        print(self.speed)

# create the object with 4 and 80 as arguments
bicycle1 = Bicycle(4,80)

# call print_attributes() using bicycle1
bicycle1.print_attributes()