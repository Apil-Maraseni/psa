import numpy as np

order = np.array([12.99, 9.99, 4.99, 12.99])

print(order * 0.8)   # Output: [10.39 7.99 3.99 10.39]

#here we dont need to use for loop as we needed in python

#another example of this is
tallest_buildings = np.array([2717, 2227, 2073, 1972, 1966, 1819, 1776])

#here we want to convert it to meter as the original one is in feet.
#we can do it easily by just multiplying it as m = ft*0.3048

print(0.3048 * tallest_buildings)
