#slicing is where we can access certain parts of a sequence
import numpy as np

# coffee = np.array([3,2,1,0,1])

# print(coffee[0:2])
# # print(coffee[1])
# print(coffee[2:])
# # print(coffee[3])
# print(coffee[-2:])

population = np.array([19571216,19673200,19854526,20104710,19463131,19544098,19593849,19636391,19657321,19653431,19626488])

print(population[:1]) #printing 1st element 
print(population[10:]) #printing last element
print(population[10:]-population[:1]) #difference between them

