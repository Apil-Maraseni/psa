# This program demonstrates exception handling in Python

# create a try block
try:
    # take input for numerator
    numerator = int(input())
    # take input for denominator
    denominator = int(input())

    # Divide numerator by denominator and print the result
    result = numerator / denominator
    print(f"Result: {result}")

# create the except block
except ZeroDivisionError:
    # Handle division by zero error
    print("Denominator cannot be 0. Try again")
