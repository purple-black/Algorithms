class Node: 
    def __init__(self,data) : 
        self.data = data
        self.link = None

class List:
    def __init__(self) :
        self.head = None 

    def create(self) :
        size = int(input("Enter the total number of nodes : "))
        if size == 0 :
            print("Empty list cannot be created")
            return
        for i in range(size) :
            val = int(input(f"Enter value for Node {i+1} : "))
            self.insert_at_end(val)

    def traversal(self) :
        if self.head is None :
            print("the list is empty")
            return
        else :
            ptr = self.head
            i = 1
            while ptr is not None :
                print(f"Node {i} : ",ptr.data)
                ptr = ptr.link
                i+=1

    def insert_at_end(self,data) :
        new = Node(data)
        if self.head is None :
            self.head = new
            return  
        ptr = self.head
        while ptr.link is not None :
            ptr = ptr.link 
        ptr.link = new 

    def insert_at_index(self,index,data) :
        if index == 1 :
            new = Node(data)
            new.link = self.head
            self.head = new
            return
        i = 1
        ptr = self.head
        while i < index-1 and ptr is not None :
            ptr = ptr.link
            i+=1
        if ptr is None :
            print("The index specified is out of bounce")
            return
        else :
            new = Node(data)
            new.link = ptr.link
            ptr.link = new 

    def insert_after_val(self,data,x) :
        ptr = self.head
        while ptr is not None :
            if ptr.data == x:
                break
            ptr = ptr.link
        if ptr is None :
            print("value specified is not found in the list")
        else :
            new = Node(data)
            new.link = ptr.link
            ptr.link = new 

    def delete(self,x) :
        if self.head is None :
            print("list is empty")
            return
        if self.head.data == x :
            self.head = self.head.link
            return
        ptr = self.head
        while ptr.link is not None :
            if ptr.link.data == x :
                break
            ptr = ptr.link
        if ptr.link is None :
            print("Specified value not found in the list")
        else :
            ptr.link = ptr.link.link

    def reverse(self) :
        ptr = self.head
        prev = None
        while ptr is not None :
            next = ptr.link
            ptr.link = prev
            prev = ptr
            ptr = next
        self.head = prev

llist = List()
llist.create() 

print("\n1.insert at end \n2.insert at index \n3.insert after value \n4.Delete \n5.reverse \n6.traversal \n7.exit")
choice = int(input("\nEnter your choice : "))

while choice != 7 :
    if choice == 1 :
        ele = int(input("Enter the value that needs to be inserted : "))
        llist.insert_at_end(ele)
        llist.traversal()
    elif choice == 2 :
        pos = int(input("Enter the position for it : "))
        ele = int(input("Enter the value that needs to be inserted : "))
        llist.insert_at_index(pos,ele)
        llist.traversal()
    elif choice == 3 :
        ele = int(input("Enter the value that needs to be inserted : "))
        val = int(input("Enter the value after which it needs to be inserted : "))
        llist.insert_after_val(ele,val)
        llist.traversal()
    elif choice == 4 :
        ele = int(input("Enter the value that needs to be deleted : "))
        llist.delete(ele)
        llist.traversal()
    elif choice == 5 :
        llist.reverse()
        llist.traversal()
    elif choice == 6 :
        llist.traversal()
    elif choice == 7 :
        exit()
    else :
        print("Enter valid choice")

    print("\n1.insert at end \n2.insert at index \n3.insert after value \n4.Delete \n5.reverse \n6.traversal \n7.exit")
    choice = int(input("\nEnter your choice : "))
            