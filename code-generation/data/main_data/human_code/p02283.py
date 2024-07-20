class binaryTree:
    def __init__(self,key,p=None,l=None,r=None):
        self.key = key
        self.p = p
        self.l = l
        self.r = r

N = int(input())
treelist = [list(input().split()) for i in range(N)]
root = None

def inorder(root):
    x = root
    if x == None:
        return
    inorder(x.l)
    
    global inlist
    inlist.append(x.key)
    
    inorder(x.r)

def insert(root,z):
    y = None
    x = root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.l
        else:
            x = x.r
    z.p = y

    if y == None:
        root = z
    elif z.key < y.key:
        y.l = z
    else:
        y.r = z
    return root
    
def outorder(root):
    x = root
    if x == None:
        return
    global outlist
    outlist.append(x.key)
    
    outorder(x.l)
    outorder(x.r)

for data in treelist:
    if data[0] == "insert":
        z = binaryTree(int(data[1]))
        root = insert(root,z)
        
    if data[0] == "print":
        inlist = []
        outlist = []
        
        inorder(root)
        indata = " " + " ".join([str(num) for num in inlist])
        print(indata)
 
        outorder(root)
        outdata = " " + " ".join([str(num) for num in outlist])
        print(outdata)
