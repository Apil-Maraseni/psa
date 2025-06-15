#Create a program to create a list of first n natural numbers using list comprehension
n = int(input("Enter a number: "))
natural_numbers = [x for x in range(1, n+1)]
print(natural_numbers)  