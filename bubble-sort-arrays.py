#bubble sort in arrays
from array import array

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                flag = 1
        if flag == 0:
            break
    return arr


my_array = array('i',[])
size = int(input("enter the size of the array: "))
for i in range(size):
    val = int(input("enter the value to be inserted: "))
    my_array.append(val)
print(my_array)

bubble_sort(my_array)
print(my_array)