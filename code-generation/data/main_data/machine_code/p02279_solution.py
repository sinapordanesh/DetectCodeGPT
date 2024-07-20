def rooted_trees(n, nodes):
    class Node:
        def __init__(self, id):
            self.id = id
            self.parent = None
            self.children = []
            self.depth = None

    tree = [Node(i) for i in range(n)]

    for node_info in nodes:
        id, k, *children = node_info
        node = tree[id]
        for child_id in children:
            child = tree[child_id]
            child.parent = node
            node.children.append(child)

    def set_depth(node, depth):
        node.depth = depth
        for child in node.children:
            set_depth(child, depth + 1)

    root = next(node for node in tree if node.parent is None)
    set_depth(root, 0)

    for node in tree:
        parent_id = node.parent.id if node.parent else -1
        node_type = "root" if node.parent is None else "leaf" if not node.children else "internal node"
        children_ids = [child.id for child in node.children]
        print(f"node {node.id}: parent = {parent_id}, depth = {node.depth}, {node_type}, {children_ids}")

# Sample Input 1
n1 = 13
nodes1 = [
    [0, 3, 1, 4, 10],
    [1, 2, 2, 3],
    [2, 0],
    [3, 0],
    [4, 3, 5, 6, 7],
    [5, 0],
    [6, 0],
    [7, 2, 8, 9],
    [8, 0],
    [9, 0],
    [10, 2, 11, 12],
    [11, 0],
    [12, 0]
]

rooted_trees(n1, nodes1)

# Sample Input 2
n2 = 4
nodes2 = [
    [1, 3, 3, 2, 0],
    [0, 0],
    [3, 0],
    [2, 0]
]

rooted_trees(n2, nodes2)