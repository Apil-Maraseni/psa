import numpy as np
arr = np.array([1,2,3]) #1d array
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr[0])
print(arr[1])
print(arr[2])

#arry with rows and columns can be printed as arr[row][column]

print(arr[0][0])
print(arr[0][2])
print(arr[2][2])

#example of rotten eggs
#Suppose we have a factory machine that determines the freshness of an egg (based on the expiration date, cracks in the shell, and smell) then assigns a number:

#✨ 100% is a healthy fresh egg.
#🤮 0% is completely rotten!

egg_carton1 = np.array([
  [0.89, 0.90, 0.83, 0.89, 0.97, 0.98], 
  [0.95, 0.95, 0.89, 0.95, 0.23, 0.99]
])

egg_carton2 = np.array([
  [0.89, 0.95, 0.84, 0.92, 0.94, 0.93], 
  [0.93, 0.95, 0.02, 0.03, 0.23, 0.99]
])

egg_carton3 = np.array([
  [0.83, 0.95, 0.89, 0.54, 0.37, 0.92], 
  [0.98, 0.99, 0.19, 0.23, 0.89, 0.91]
])

print("average freshness of cartoon 1 is ",np.average(egg_carton1))
print("average freshness of cartoon 2 is ",np.average(egg_carton2))
print("average freshness of cartoon 3 is ",np.average(egg_carton3))
#np.average() is a built in function to find the average of the array numbers or any kind of numbers.
