#selection sort on arrays
from array import array

def selection_sort(arr):
    sz = len(arr)
    for i in range(sz-1):
        imin = i
        for j in range(i+1,sz):
            if arr[j] < arr[imin]:
                imin = j
            temp = arr[i]
            arr[i] = arr[imin]
            arr[imin] = temp
    return arr



my_array = array('i',[])
size = int(input("enter the size of the array: "))
for i in range(size):
    val = int(input("enter the value to be inserted: "))
    my_array.append(val)
print(my_array)

selection_sort(my_array)
print(my_array)