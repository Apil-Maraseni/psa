# This code demonstrates exception handling in Python.

# create a try block
try:
    cars = ['BMW', 'Ferrari', 'Audi', 'Tesla']

    # take integer input
    index = int(input())

    # print the item from the cars list
    print(cars[index])
# create the except block
except:
    print("Wrong Index")