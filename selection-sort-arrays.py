# insertion sort on arrays

from array import array

def selection_sort(x):
    for i in range(len(x)):
        imin = i
        for j in range(i+1,len(x)):
            if x[j] < x[imin]:
                imin = j
        temp = x[imin]
        x[imin] = x[i]
        x[i] = temp


x = array('i',[])

for i in range(0,5):
    val = int(input("enter value for array: "))
    x.append(val)

print(x)
selection_sort(x)
print(x)

