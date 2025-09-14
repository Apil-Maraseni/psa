#some common functions are as follows
# .min() Return the minimum value of an array.
# .max() Return the maximum value of an array.
# .sum() Return the total sum of an array's values.
# .average() Return the average value of an array.

import numpy as np
temperatures = np.array([[50, 51, 54, 59, 59, 53, 54, 51],
                         [45, 50, 38, 44, 40, 46, 43, 39]])

print(np.min(temperatures))       # Output: 38
print(np.max(temperatures))       # Output: 59
print(np.sum(temperatures))       # Output: 776
print(np.average(temperatures))   # Output: 48.5

#AXIS
# by specifying the axis parameter, we can apply an operation along the specified axis of an array

print(np.sum(temperatures, axis=0)) #axis=0 each column
print(np.min(temperatures, axis=1)) #axis = 1 each row

steps = np.array([5240, 6789, 8342, 9100, 7563, 10234, 8931])
print(np.min(steps))
print(np.max(steps))
print(np.sum(steps))
print(np.average(steps))
