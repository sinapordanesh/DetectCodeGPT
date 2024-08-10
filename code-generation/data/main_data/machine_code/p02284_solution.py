def binary_search_tree_operations(operations):
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def insert(root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
        return root

    def find(root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return find(root.left, key)
        else:
            return find(root.right, key)

    def inorder_walk(root):
        if root is not None:
            inorder_walk(root.left)
            print(f" {root.key}", end="")
            inorder_walk(root.right)

    def preorder_walk(root):
        if root is not None:
            print(f" {root.key}", end="")
            preorder_walk(root.left)
            preorder_walk(root.right)

    root = None
    for operation in operations:
        if operation[0] == 'insert':
            key = int(operation[1])
            root = insert(root, key)
        elif operation[0] == 'find':
            key = int(operation[1])
            if find(root, key):
                print("yes")
            else:
                print("no")
        elif operation[0] == 'print':
            inorder_walk(root)
            print()
            preorder_walk(root)

# Sample input
operations = [
    ['insert', '30'],
    ['insert', '88'],
    ['insert', '12'],
    ['insert', '1'],
    ['insert', '20'],
    ['find', '12'],
    ['insert', '17'],
    ['insert', '25'],
    ['find', '16'],
    ['print']
]

binary_search_tree_operations(operations)