import numpy as np
#here is a list of passengers of titanic with passenger id, alive or dead, passenger class and their age
passengers = np.array([
   [1, 0, 3, 22],
   [2, 1, 1, 38],
   [3, 1, 3, 26],
   [4, 1, 1, 35],
   [5, 0, 3, 35],
   [6, 0, 3, 18],
   [7, 0, 1, 54],
   [8, 0, 3, 2],
   [9, 1, 3, 27],
  [10, 1, 2, 14],
  [11, 1, 3, 4],
  [12, 1, 1, 58],
  [13, 0, 3, 20],
  [14, 0, 3, 39],
  [15, 0, 3, 14],
  [16, 1, 2, 55],
  [17, 0, 3, 2],
  [18, 1, 2, 12],
  [19, 0, 3, 31],
  [20, 1, 3, 8],
  [21, 0, 2, 35],
  [22, 1, 2, 34],
  [23, 1, 3, 15],
  [24, 1, 1, 28],
  [25, 0, 3, 8],
  [26, 1, 3, 38],
  [27, 0, 3, 2],
  [28, 0, 1, 1],
  [29, 1, 3, 5],
  [30, 0, 3, 18],
  [31, 0, 1, 40],
  [32, 1, 1, 70],
  [33, 1, 3, 33],
  [34, 0, 2, 66],
  [35, 0, 1, 28],
  [36, 0, 1, 42],
  [37, 1, 3, 5],
  [38, 0, 3, 18],
  [39, 0, 3, 18],
  [40, 1, 3, 14],
  [41, 0, 3, 40],
  [42, 0, 2, 27],
  [43, 0, 3, 29],
  [44, 1, 2, 0],
  [45, 1, 3, 19],
  [46, 0, 3, 33],
  [47, 0, 3, 14],
  [48, 1, 3, 22],
  [49, 0, 3, 41],
  [50, 0, 3, 18]
])

#shape of the array
print(passengers.shape)

#average age of passengers
print(np.average(passengers[:,3]))

#oldest passenger
oldest = np.argmax(passengers[:,3])
print(oldest)

#youngest passenger
youngest = np.argmin(passengers[:,3])
print(youngest)

#passsenger number of oldest passenger
old_number = passengers[oldest,0]
print(old_number)

#percentage of folks that survived
survived = (np.average(passengers[:,1]))*100
print(survived)

#percentage of folks that survivied according their classes
#for class 1
class1 = passengers[passengers[:,2] == 1]
total_class1 = len(class1)

survived_class1 = np.sum(class1[:,1])
percentage1 = (survived_class1/total_class1)*100

print("survival percentage of class 1 is",percentage1)

#for class2
class2 = passengers[passengers[:,2]==2]
total_class2 = len(class2)

survived_class2 = np.sum(class2[:,1])
percentage2 = (survived_class2/total_class2)*100

print("survival percentage of class 2 is", percentage2)

#for class 3
class3 = passengers[passengers[:,2]==3]
total_class3 = len(class3)

survived_class3 = np.sum(class3[:,1])
percentage3 = (survived_class3/total_class3)*100

print("survival percentage of class 3 is", percentage2)

#in this way we can finish the simple program using all the concepts of chapter 2 operations
