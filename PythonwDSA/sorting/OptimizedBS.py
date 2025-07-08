#Since each outer loop iteration places an element in its final position (from right to left), we can optimize our code by reducing the number of inner loop comparisons.
def bubble_sort(lst):
    size = len(lst)
    for i in range(size):
        for j in range(size-1-i):  #this program doesnt compare already sorted element i.e from the last
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

data_list = [9,6,1,4,2]

sorted_list = bubble_sort(data_list)
print(sorted_list)


#if no swapping occurs; terminate the program
def bubble_sort(lst):
    size = len(lst)
    for i in range(size):
        swapped = False
        for j in range(size-1-i):  #this program doesnt compare already sorted element i.e from the last
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

data_list = [9,6,1,4,2]

sorted_list = bubble_sort(data_list)
print(sorted_list)


#use cases:
# small datasets
# when simplicity is more importnat than efiiciency
# when data is already partially sorted