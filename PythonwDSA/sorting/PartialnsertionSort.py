#partial insetion sort

def perform_partial_sort(lst,n):
    for i in range (1,n):
        key = lst[i]
        j = i-1
        while j>=0 and key <= lst[j]:
            lst[j+1]= lst[j]
            j=j-1
            lst[j+1]= key
    return lst[:n]


data = list(map(int, input("Enter numbers separated by space: ").split()))

n= int(input("Enter the number of elements to sort: "))
if n > len(data):
    print("n is larger than the list length. Sorting the entire list.")
    n = len(data)

sorted_data = perform_partial_sort(data, n)
print("Partially sorted list:", sorted_data)