class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    
def circle(head):
    if head == None:
        return True
 
    
    node = head.next
    
    while((node is not None) and (node is not head)):
        
        node = node.next
 
    return(node == head)



linklist = List()
linklist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

linklist.head.next = second
second.next = third
third.next = fourth

if (circle(linklist.head)):
    print('Yes')
else:
    print('No')         #now, it is a linear linked list
 
fourth.next = linklist.head #now its a circular linked list
 
if (circle(linklist.head)):
    print('Yes')
else:
    print('No')