#for loop doesnot use index so we use enumerate to get index and value

languages = ["Python", "Java", "C++", "JavaScript"]
enumerate_languages = enumerate(languages)

print(list(enumerate_languages))  # Output: [(0, 'Python'), (1, 'Java'), (2, 'C++'), (3, 'JavaScript')]


for index, language in enumerate(languages):
    print(index, language)







animals = ['Dog', 'Cat']
wild_animals = ['Tiger', 'Coyote']

# perform list operations
animals.insert(2,'Raccoon')

animals.extend(wild_animals)
animals.pop(2)

animals.pop()

animals.insert(2,'Moose')

print(animals)


