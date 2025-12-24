#9. bubble sort algorithm

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

lst = []
n = int(input("Enter number of elements: "))
for i in range(n):
    lst.append(int(input("Enter element:")))
    
print("Original List:", lst)
sort_list = bubble_sort(lst)
print("Sorted List (Ascending):", sort_list)
