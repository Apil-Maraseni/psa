# Write a program to create a function that can take a variable number of arguments and returns the product of numbers passed as arguments.

# create the function
def multiply_numbers(*args):
    mul =1
    for i in args:
        mul*=i
    return mul

# get three integer inputs
n1 = int(input())
n2 = int(input())
n3 = int(input())

# call the function
result = multiply_numbers(n1,n2,n3)

# print the result
print(result)
