#linkedlist - traversals

class Node: 
    def __init__(self,data) : 
        self.data = data
        self.link = None

class List:
    def __init__(self):
        self.head = None
    
    def create(self):
        size = int(input("enter the number of nodes: "))
        if size == 0:
            print("enter valid number, empty list!")
            return
        for i in range(size):
            val = int(input(f"enter element at node {i+1}: "))
            self.insert_end(val)

    def insert_end(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        ptr = self.head
        while ptr.link is not None:
            ptr = ptr.link
        ptr.link = new

    def traverse(self):
        if self.head is None:
            print("empty list!")
            return
        ptr = self.head
        print("List: ")
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.link
        return

    


def reversetrav(ptr):
    if ptr is None:
        return
    reversetrav(ptr.link)
    print(ptr.data)

    

llist = List()
llist.create()
print("list in forward order: ")
llist.traverse()
p = llist.head
print("list in reverse order: ")
reversetrav(p)












        




