import numpy as np
#.arrange() function aka array range analogous to .range() function used in python in for loop. it creates an array with evenly spaced values.

arr = np.arange(start = 1, stop = 10, step = 3)
print(arr)

#Halley's Comet is a comet visible from earth every 75 years. so we will fins in which year it will be seen within 3000 yrs range from 1986
comete = np.arange(start = 1986, stop = 3000, step = 75)
print(comete)