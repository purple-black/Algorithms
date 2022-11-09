class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.head = None

def display(head):
    ptr = head
    while ptr is not None:
        print(ptr.data)
        ptr = ptr.next

def sortinsert(head,curr):
    temp = None
    if head == None:
        head = curr
    
    elif head.data >= curr.data:
        curr.next = head
        curr.next.prev = curr
        head = curr

    else:
        temp = head
        while temp.next is not None and temp.next.data < curr.data:
            temp = temp.next

        curr.next = temp.next

        if temp.next is not None:
            curr.next.prev = curr

        temp.next = curr
        curr.prev = temp
    return head

def insertionsort(head):
    curr = head
    sortedhead = None
    while curr is not None:
        curnext = curr.next
        curr.next = curr.prev = None
        sortedhead = sortinsert(sortedhead, curr)
        curr = curnext

    return sortedhead


list = List()
list.head = Node(4)
second = Node(1)
third = Node(10)
fourth = Node(2)
fifth = Node(5)
list.head.next = second
second.prev = list.head
second.next = third
third.prev = second
third.next = fourth
fourth.next = fifth
fourth.prev = third

print("linked list is: ")
display(list.head)
shead = insertionsort(list.head)
print("linked list after insertion sort is: ")
display(shead)