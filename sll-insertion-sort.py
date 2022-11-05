class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

def display(head):
    ptr = head
    while ptr is not None:
        print(ptr.data)
        ptr = ptr.next

def sortinsert(head,curr):
    if head == None or head.data >= curr.data:
        curr.next = head
        return curr

    temp = head
    while temp.next is not None and temp.next.data < curr.data:
        temp = temp.next
    curr.next = temp.next
    temp.next = curr
    return head

def insertionsort(head):
    curr = head
    sortedhead = None
    while curr is not None:
        curnext = curr.next
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
second.next = third
third.next = fourth
fourth.next = fifth

print("linked list is: ")
display(list.head)
shead = insertionsort(list.head)
print("linked list after insertion sort is: ")
display(shead)