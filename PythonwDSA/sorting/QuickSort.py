#quick sort
#sekects a random element of the list as a pivot and partitions the reamining elemnets into two subklists: those less tahn the pivot and those greater than the pivot
#the sublists are then sorted recursively
def quick_sort(lst):
    length = len(lst)

    if length <= 1:
        return lst
    else:
        pivot = lst.pop()
    
    right = []
    left = []
    for element in lst:
        if element > pivot:
            right.append(element)
        else:
            left.append(element)
        
    return quick_sort(left) + [pivot] + quick_sort(right)

lst = [7,2,1,6,8,5,3,4]
print(f"unsorted list: {lst}")
sorted_list = quick_sort(lst)
print(f"sorted list: {sorted_list}")

#descending order 

def quick_sort(lst):
    # write you code here    
    length = len(lst)
    if length <=1 :
        return lst
    else:
        pivot = lst.pop()
    
    right =[]
    left = []
    for element in lst:
        if element > pivot:
            left.append(element)
        else:
            right.append(element)
    return quick_sort(left) + [pivot] + quick_sort(right)

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = quick_sort(data_list)

print(sorted_list)