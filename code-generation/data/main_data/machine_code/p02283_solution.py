def insert(T, z):
    y = None
    x = T
    while x:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y

    if y == None:
        T = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

def inorder_walk(node):
    if node:
        inorder_walk(node.left)
        print(node.key, end=' ')
        inorder_walk(node.right)

def preorder_walk(node):
    if node:
        print(node.key, end=' ')
        preorder_walk(node.left)
        preorder_walk(node.right)

m = int(input().strip())
T = None

for _ in range(m):
    op = input().strip().split()
    if op[0] == 'insert':
        if not T:
            T = Node(int(op[1]))
        else:
            insert(T, Node(int(op[1])))
    elif op[0] == 'print':
        inorder_walk(T)
        print()
        preorder_walk(T)