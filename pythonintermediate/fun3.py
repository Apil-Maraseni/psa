# Write a program to create a function that can take a variable number of keyword arguments.
#Expected Output
#{'first':'joe', 'last': 'biden'}
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with keyword arguments
first = input("Enter first name: ")
last = input("Enter last name: ")
print_info(first=first, last=last)
# Expected Output
#{'first':'joe', 'last': 'biden'}
