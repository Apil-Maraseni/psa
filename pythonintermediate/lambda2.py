# This code defines a lambda function to compute the square root of two numbers and prints the result.

# create the function
compute = lambda x,y : x**0.5 + y**0.5

# take two integer inputs
n1 = int(input())
n2 = int(input())

# call the function and print the result
print(compute(n1,n2))