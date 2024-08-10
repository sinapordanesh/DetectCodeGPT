def binary_search_tree_operations(m, operations):
    import sys
    input = sys.stdin.readline
    output = sys.stdout.write
    
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
        elif key > root.key:
            root.right = insert(root.right, key)
        return root

    def find(root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return find(root.left, key)
        return find(root.right, key)

    def minValueNode(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def deleteNode(root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = deleteNode(root.left, key)
        elif key > root.key:
            root.right = deleteNode(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = minValueNode(root.right)
            root.key = temp.key
            root.right = deleteNode(root.right, temp.key)
        return root

    def inorder(root, result):
        if root:
            inorder(root.left, result)
            result.append(root.key)
            inorder(root.right, result)

    def preorder(root, result):
        if root:
            result.append(root.key)
            preorder(root.left, result)
            preorder(root.right, result)

    tree = None
    inorder_result = []
    preorder_result = []

    for i in range(m):
        op, *args = operations[i].split()
        if op == 'insert':
            key = int(args[0])
            tree = insert(tree, key)
        elif op == 'find':
            key = int(args[0])
            if find(tree, key):
                output("yes\n")
            else:
                output("no\n")
        elif op == 'delete':
            key = int(args[0])
            tree = deleteNode(tree, key)
        elif op == 'print':
            inorder_result = []
            inorder(tree, inorder_result)
            output(" ".join(map(str, inorder_result)) + "\n")
            preorder_result = []
            preorder(tree, preorder_result)
            output(" ".join(map(str, preorder_result)) + "\n")

# Sample input
binary_search_tree_operations(18, ["insert 8", "insert 2", "insert 3", "insert 7", "insert 22", "insert 1", "find 1", "find 2", "find 3", "find 4", "find 5", "find 6", "find 7", "find 8", "print", "delete 3", "delete 7", "print"])