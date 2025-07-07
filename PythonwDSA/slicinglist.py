#slicing a list
numbers = [10,20,30,40,50,60]
new_numbers = numbers[2:5]
print(new_numbers)  # Output: [30, 40, 50]  

print(numbers[0:4])  # Output: [10, 20, 30, 40]
print(numbers[3:5])  # Output: [40, 50]

print(numbers[3:-1])  # Output: [40, 50] # Slicing with negative index item from 4th to second last iten


animals = ['dog', 'cat', 'guinea pig', 'rat']

# extract elements using list slicing
new_animals = animals[1:3]

# print the new list
print(new_animals)  # Output: ['cat', 'guinea pig']

print(numbers[:4])  # Output: [10, 20, 30, 40] #items from start to 4th item
print(numbers[3:])  # Output: [40, 50, 60] #items from 4th to last item
print(numbers[:])  # Output: [10, 20, 30, 40, 50, 60] # all items in the list