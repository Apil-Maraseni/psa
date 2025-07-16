#middle element as pivot

def quick_sort(lst):
    length = len(lst)
    if length <=1 :
        return lst
    else:
        pivot = lst[length//2]
        left = [x for x in lst if x < pivot]
        middle = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

data_list = list(map(int, input().split()))

sorted_list = quick_sort(data_list)
print(sorted_list)