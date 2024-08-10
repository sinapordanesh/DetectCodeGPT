class node():
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
 
 
class binarysearchtree(list):
    def __init__(self):
        list.__init__(self)
        self.root = None
 
    def insert(self, z):
        z = node(z)
        y = None
        x = self.root
 
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
 
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
 
    def inorder(self):
        def inparse(u):
            if u == None:
                return
            inparse(u.left)
            print(" " + str(u.key), end="")
            inparse(u.right)
        inparse(self.root)
        print("")

    def outorder(self):
        def outparse(u):
            if u == None:
                return
            print(" " + str(u.key), end="")
            outparse(u.left)
            outparse(u.right)
        outparse(self.root)
        print("")
 
    def print(self):
        self.inorder()
        self.outorder()
 
    def find(self, k):
        x = self.root
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x
 
n = int(input())
clist = [input().split(" ") for i in range(n)]
tree = binarysearchtree()

for c in clist:
    if c[0] == "insert":
        tree.insert(int(c[1]))
    elif c[0] == "find":
        f = tree.find(int(c[1]))
        if f is None:
            print("no")
        else:
            print("yes")
    else:
        tree.print()
