# #inserion sorting algorithm
# take elements one by one and insert them in the right place in the sorted part of the array
# # Time complexity: O(n^2)



def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        # compare the key element with elements to its left one by one
        # end the loop if the key element is larger or equal
        while j >= 0 and key <= lst[j]:
            # shift the element to its right
            lst[j + 1] = lst[j]
            # decrease j to go to the next element to its left
            j = j - 1

        # insert the key element to the correct position
        lst[j + 1] = key
    return lst

data = [7,4,1,3,2]
print(f"unsorted list: {data}")
sorted_list = insertion_sort(data)
print(f"sorted list: {sorted_list}")

# in descending order
def insertion_sort_desc(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        # compare the key element with elements to its left one by one
        # end the loop if the key element is smaller or equal
        while j >= 0 and key >= lst[j]:
            # shift the element to its right
            lst[j + 1] = lst[j]
            # decrease j to go to the next element to its left
            j = j - 1

        # insert the key element to the correct position
        lst[j + 1] = key
    return lst
data = list(map(int, input().split()))
sorted_list = insertion_sort_desc(data)
print(f"sorted list in descending order: {sorted_list}")
# Swap this element with the second element.