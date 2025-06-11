# This code demonstrates inheritance in Python by creating a base class Vehicle
# and a derived class Car. The Car class inherits features from the Vehicle class.

# create the Vehicle class
class Vehicle:
    # define get_vehicle_features()
    def get_vehicle_features(self):
        print("Initializing vehicle features")

# derive the Car class from Vehicle 
class Car(Vehicle):
    # define get_car_features()
    def get_car_features(self):
        print("Initializing car features")

# create an object of the Car class
lambo = Car()

# call get_vehicle_features() using the object
lambo.get_vehicle_features()

# call get_car_features() using the object
lambo.get_car_features()



