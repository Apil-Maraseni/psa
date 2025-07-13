# Merge sort breaks a list into multiple sublists, and each sublist is then sorted individually.
# Then the sorted sublist are combined to form the sorted list.
# Follows divide and conquer strategy


def merge_sort(lst):
    if len(lst)<=1:
        return lst
    
    mid = len(lst) //2
    left_partition = merge_sort(lst[:mid])
    right_partition = merge_sort(lst[mid:])

    return merge(left_partition, right_partition)

def merge(left, right):
    output = []
    i=0
    j=0

    while i < len(left) and j< len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i+=1
        else:
            output.append(right[j])
            j+=1
    output.extend(left[i:])
    output.extend(right[j:])

    return output

data_list = [6,8,1,4,5,3,7,2]
print(f"Unsorted: {data_list}")

result = merge_sort(data_list)

print(f"sorted: {result}")
