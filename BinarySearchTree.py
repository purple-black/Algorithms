class Node :
    def __init__(self,data) :
        self.left = None
        self.right = None
        self.data = data

    def create(self):
        num = int(input("enter no of nodes: "))
        for i in range(num):
            data = int(input("enter value for node: "))
            self.add(data)

    def add(self,data):
        new = Node(data)
        if root.right is None and root.left is None: #if only root node is there
            if data > root.data:
                root.right = new    #inserting new node and return
                return
            elif data < root.data:
                root.left = new     #inserting new node and return
                return
            else:
                print("duplication\n") # in bst, 1 element only once
                return
        ptr = root   # if it is not only the root node 
        par = None      # par points the parent node of the ptr in each step
        while ptr is not None:
            if data > ptr.data:
                par = ptr
                ptr = ptr.right
                if ptr is None:
                    par.right = new
                    return
                else:
                    continue
            elif data < ptr.data:
                par = ptr
                ptr = ptr.left
                if ptr is None:
                    par.left = new
                    return
                else:
                    continue

def inorder(root):
    current = root
    stack = [] # initialize stack
    
    while True:
        if current is not None:
            stack.append(current)
            current = current.left # go till the left most and then pop one by one,
                                   #print and each time going to its corresponding right also

        elif(stack):
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
 
        else:
            break

def search(root,key):
    curr = root
    while curr is not None:
        if key > curr.data :  # check right subtree
            curr = curr.right 

        elif key < curr.data : #check left subtree
            curr = curr.left

        else :
            return True #if its equal got the element
    return False

def preorder(root):
    if root is None:
        print("empty tree")
        return
    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        print(node.data)
        if node.right is not None: # first push right child on to stack and then left
            stack.append(node.right)  #so left is accessed first (preorder -- R0 L R)
        if node.left is not None:
            stack.append(node.left)





root = Node(int(input("enter root node: ")))
root.create()
inorder(root)
key = int(input("enter elemnt to be searched: "))
flag = search(root,key)
if flag == True:
    print("element found!\n")
else:
    print("element not present!\n")

preorder(root)
#insert element
root.add(11)
inorder(root)


