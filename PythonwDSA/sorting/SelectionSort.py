# #selection sort
# Here's how it works:

# Select the smallest element from the list.
# Swap this element with the first element.
# At this point, the correct element is placed at the first position. However, the portion of the list from the second position to the last remains unsorted. Therefore,

# Select the smallest element from the remaining unsorted part (from the second to last positions) of the list.
# Swap this element with the second element.
# Continue this process for each following position until the entire list is sorted


def selection_sort(lst):

    for i in range(len(lst)):

        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[min_index], lst[i] = lst[i], lst[min_index]
    return lst

data = [18,10,8,14,1]
print(f"unsorted list: {data}")

sorted_list = selection_sort(data)
print(f"sorted list: {sorted_list}")

#selection sort in descending order
def selection_sort(lst):
    # write your code here
    size = len(lst)

    for i in range (size):
        min_index = i

        for j in range(i+1, size):
            if lst[j] > lst[min_index]:
                min_index = j
        lst[min_index], lst[i] = lst[i], lst[min_index]
    return lst
             
# take integer input and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = selection_sort(data_list)
print(sorted_list)