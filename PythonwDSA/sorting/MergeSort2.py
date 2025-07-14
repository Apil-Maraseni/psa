#nth smallest element of two sorted list
def find_nth_smallest(lst1, lst2, n):
    merged = merge_sorted_lists(lst1, lst2)
    if n-1 < len(merged):
        return merged[n-1]
    return None

def merge_sorted_lists(lst1, lst2):
    merged = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])
    return merged
