#hare and tortoise algorithm to find it the given link is circular linked list or not

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


def check(head):   
    #hare and tortoise algorithm
    #t for tortoise and h for hare
    t = head       
    h = head     
    if head.next is None:
        return False
    while h is not None and h.next is not None:  
        t = t.next
        h = h.next.next

        if t == h:
            return True
    return False
    

mylist = List()
mylist.head = None
c = 1
while c < 6:
    val = int(input(f"enter value for Node {c}: "))
    if mylist.head is None:
        mylist.head = Node(val)
    ptr = mylist.head
    while ptr.next is not None:
        ptr = ptr.next
    ptr.next = Node(val)
    c+=1
ptr = ptr.next

print("enter choice : 1. circular-connect to head or 2.circular-to other nodes or 3. linear")
choice = int(input())
if choice == 1:
    ptr.next = mylist.head
elif choice == 2:
    ptr.next = mylist.head.next #here connected to the second node
else:
    ptr.next = None


#display(mylist.head)
result = check(mylist.head)
if result == True:
    print("The given linked list is circular")
else:
    print("The given linked list is linear")