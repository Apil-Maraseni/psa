#Create a program to create a dictionary using dictionary comprehension.
numbers = [1, 2, 3, 4]

# create the dictionary using comprehension
result ={x: x+1 for x in numbers}      # key: value pairs

# print the dictionary
print(result)