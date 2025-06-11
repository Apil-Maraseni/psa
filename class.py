# Replace ___ with your code

class Triangle:
    
    # initialize attributes
    def __init__(self, a, b, c):
        self.s1 = a
        self.s2 = b
        self.s3 = c

    # method to compute perimeter
    # Hint: you don't need to pass additional arguments to solve this problem
    def get_perimeter(self):
        perimeter = self.s1 + self.s2 + self.s3
        return perimeter

# take three integer inputs
a = int(input())
b = int(input())
c = int(input())

# create an object of Triangle
train = Triangle(a,b,c)


# call the get_perimeter() method using the object
result = train.get_perimeter()

print(result)