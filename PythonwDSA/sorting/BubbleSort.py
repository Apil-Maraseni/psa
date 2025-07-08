#Bubble Sort
#it works by repeatedly comparing two adjacent elements and swapping them if they are not in correct order.

def bubble_sort(lst):
  
 size = len(lst)
 for i in range(size):  #this loop to access all the element 
   for j in range(size-1):  #this loop to comapre list elements

    if lst[j] > lst[j+1]:
    #swap the element
       lst[j], lst[j+1] = lst[j+1], lst[j]
 return lst

data_list = [15,16,6,8,5]
print(f"unsorted list: {data_list}")

sorted_list = bubble_sort(data_list)

print(f"sorted list: {sorted_list}")

#Bubble sort in descending order

def bubble_sort(lst):
    # write your code here
    size = len(lst)
    for i in range(size):
        for j in range(size-1):
           if lst[j] < lst [j+1]:
            lst[j], lst[j+1] = lst[j+1],lst[j]
    return lst

# take integer inputs and convert it to a list    
data_list = list(map(int, input().split()))

sorted_list = bubble_sort(data_list)
print(sorted_list)