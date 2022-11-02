class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def create(self):
        size = int(input("enter number of nodes: "))
        if size == 0:
            print("empty list! enter valid number")
            return
        for i in range(size):
            val = int(input(f"enter value at node {i+1}: "))
            self.insert_end(val)


    def insert_end(self,data):
        if self.head is None:
            new =  Node(data)
            self.head = new
            return
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        new =  Node(data)
        ptr.next = new
        new.prev = ptr

    def insert_index(self,index,data):
        if index == 1:
            new = Node(data)
            new.next = self.head
            self.head.prev = new
            self.head = new
            return
        ptr = self.head
        i = 1
        while i < index - 1 and ptr is not None:
            ptr = ptr.next
            i+=1
        if ptr is None:
            print("index out of bounds")
        else:
            new = Node(data)
            new.next = ptr.next
            new.prev = ptr
            ptr.next.prev = new
            ptr.next = new

    def delete(self,x):
        if self.head is None:
            print("the list is empty")
            return
        if self.head.data == x:
            self.head = self.head.next
            self.head.prev = None
            return

        ptr = self.head
        while ptr.next is not None:
            if ptr.data  == x:
                break
            ptr = ptr.next
        if ptr.next is None:
            if ptr.item == x:
                ptr.prev.next = None
            else:
                print("item not found in list")
        else:
            ptr.prev.next = ptr.next
            ptr.next.prev = ptr.prev

    def ftraverse(self):
        ptr = self.head
        print("list is: ")
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

def revtraversal(ptr):
    if ptr is None:
        return
    revtraversal(ptr.next)
    print(ptr.data)
            






llist = List()
llist.create()


print("\n1.Insert at index \n2.delete \n3.revtraversal \n4.ftraverse\n") 
choice = int(input("Enter your choice : "))

while choice != 5 :
    if choice == 1 :
        pos = int(input("Enter the position for it : "))
        ele = int(input("Enter the value that needs to be inserted : "))
        llist.insert_index(pos,ele)
        llist.ftraverse()
    elif choice == 2 :
        ele = int(input("Enter the value that needs to be deleted : "))
        llist.delete(ele)
        llist.ftraverse()
    elif choice == 3 :
        p = llist.head
        revtraversal(p)
    elif choice == 4 :
        llist.ftraverse()
    else : 
        print("Enter valid Choice")
        
    print("\n1.Insert at index \n2.delete \n3.revtraversal \n4.ftraverse\n")  
    choice = int(input("Enter your choice : "))




            




