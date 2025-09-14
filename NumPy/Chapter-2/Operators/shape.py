import numpy as np

#NumPy arrays have a property called .shape that returns a tuple containing number of elements each dimension has.
arr = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print(arr.shape)
#it gives number of rows and columns present in that array.

#to convert 1 dimensional array into two dimensional ones we can use .reshape() function .
#for example

arr = np.array([1,2,3,4,5,6,7,8])
new_arr = arr.reshape(2,4)

print(new_arr)

#another example is:
month_results = np.array([56, 100, 33, 0, 45, 45, 46, 34, 89, 180, 60, 45, 45, 44, 46, 45, 0, 0, 15, 90, 301, 197, 20, 60, 45, 45, 42, 45])
print(month_results.shape)
new = month_results.reshape(4,7)
print(new)