# this is the same as the previous code, but it uses the super() function to call the eat() method from the Animal class.

# create the Animal class
class Animal:
    def eat(self):
        print("I can eat food")


# create the Dog class
class Dog(Animal):
    def bark(self):
        print("I can bark")
    
    def eat(self):
        super().eat()

# create an object of the Dog class
d1 = Dog()

# call the eat() method using the object
d1.eat()


