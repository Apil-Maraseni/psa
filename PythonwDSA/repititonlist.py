# Repeating elements in a list
list = [0] * 5
print(list)  # Output: [0, 0, 0, 0, 0] #created a list with 5 elements, all initialized to 0

#Methods             Description
# append()           Adds an element to the end of the list 
# extend()          Adds multiple elements to the end of the list
# insert()          Adds an element at a specified position in the list
# pop()             Removes and returns the last element of the list
# reverse()         Reverses the order of the elements in the list

currencies = ["Dollar", "Euro", "Pound"]
currencies.append("Yen")

print(currencies)  # Output: ['Dollar', 'Euro', 'Pound', 'Yen'] #added Yen to the end of the list

prime_numbers = [2, 3, 5, 7]
removed_element = prime_numbers.pop(2)  # Removes the element at index 2 (5 in this case)
print(f"Updated List: {prime_numbers}")  # Output: Updated List: [2, 3, 7]
print(f"Removed Element: {removed_element}")  # Output: Removed Element: 5  

prime_numbers.pop()  # Removes the last element (7 in this case)
print(f"List after pop: {prime_numbers}")  # Output: List after pop: [2, 3]

#list insert
vowels = ['a','e','i','u']
vowels.insert(3,'o')
print(vowels)  # Output: ['a', 'e', 'i', 'o', 'u'] #inserted 'o' at index 3

#list reverse
prime_numbers.reverse()
print(prime_numbers)
