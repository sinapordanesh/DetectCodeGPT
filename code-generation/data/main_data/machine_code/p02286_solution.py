def rightRotate(t):
    s = t.left
    t.left = s.right
    s.right = t
    return s

def leftRotate(t):
    s = t.right
    t.right = s.left
    s.left = t
    return s

class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None

def insert(t, key, priority):
    if t is None:
        return Node(key, priority)
    if key == t.key:
        return t
    if key < t.key:
        t.left = insert(t.left, key, priority)
        if t.priority < t.left.priority:
            t = rightRotate(t)
    else:
        t.right = insert(t.right, key, priority)
        if t.priority < t.right.priority:
            t = leftRotate(t)
    return t

def delete(t, key):
    if t is None:
        return None
    if key < t.key:
        t.left = delete(t.left, key)
    elif key > t.key:
        t.right = delete(t.right, key)
    else:
        return _delete(t, key)
    return t

def _delete(t, key):
    if t.left is None and t.right is None:
        return None
    elif t.left is None:
        t = leftRotate(t)
    elif t.right is None:
        t = rightRotate(t)
    else:
        if t.left.priority > t.right.priority:
            t = rightRotate(t)
        else:
            t = leftRotate(t)
    return delete(t, key)

def inorder(t):
    if t:
        inorder(t.left)
        print(f" {t.key}", end='')
        inorder(t.right)

def preorder(t):
    if t:
        print(f" {t.key}", end='')
        preorder(t.left)
        preorder(t.right)

m = int(input())
root = None

for _ in range(m):
    operation = input().split()
    if operation[0] == "insert":
        key, priority = map(int, operation[1:])
        root = insert(root, key, priority)
    elif operation[0] == "find":
        key = int(operation[1])
        if find(root, key):
            print("yes")
        else:
            print("no")
    elif operation[0] == "delete":
        key = int(operation[1])
        root = delete(root, key)
    elif operation[0] == "print":
        inorder(root)
        print()
        preorder(root)