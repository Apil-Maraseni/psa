# This code defines a class `Square` with methods to compute the area and perimeter of a square.

# create the class
class Square:

    # define the __init__() method
    def __init__(self,length):
        self.length = length
  
    # define the compute_area() method
    def compute_area(self):
        area = self.length * self.length
        return area
    
    # define the compute_perimeter() method
    def compute_perimeter(self):
        perimeter = 4* self.length
        return perimeter


# get integer input
length = int(input())

# create an object of Square    
sq = Square(length)

# call compute_area() and print the area
print (sq.compute_area())

# call compute_perimeter() and print the perimeter
print(sq.compute_perimeter())