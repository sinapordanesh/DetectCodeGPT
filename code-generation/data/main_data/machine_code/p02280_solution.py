def binary_tree_info(n, nodes):
    tree = {}
    for i in range(n):
        node_id, left, right = nodes[i]
        tree[node_id] = {"parent": None, "children": [], "depth": 0, "height": 0}

        if left != -1:
            tree[node_id]["children"].append(left)
            tree[left] = {"parent": node_id, "children": [], "depth": 0, "height": 0}
        if right != -1:
            tree[node_id]["children"].append(right)
            tree[right] = {"parent": node_id, "children": [], "depth": 0, "height": 0}

    def update_depth_height(node_id, depth):
        tree[node_id]["depth"] = depth
        max_child_height = 0
        for child_id in tree[node_id]["children"]:
            update_depth_height(child_id, depth + 1)
            max_child_height = max(max_child_height, tree[child_id]["height"])
        tree[node_id]["height"] = max_child_height + 1

    root = None
    for node_id in tree:
        if tree[node_id]["parent"] is None:
            root = node_id
            break

    update_depth_height(root, 0)

    for node_id in tree:
        parent = tree[node_id]["parent"]
        sibling = None
        if parent is not None:
            sibling = [child_id for child_id in tree[parent]["children"] if child_id != node_id][0]
        deg = len(tree[node_id]["children"])
        depth = tree[node_id]["depth"]
        height = tree[node_id]["height"]
        node_type = "root" if parent is None else "leaf" if deg == 0 else "internal node"
        print(f"node {node_id}: parent = {parent}, sibling = {sibling}, degree = {deg}, depth = {depth}, height = {height}, {node_type}")

n = 9
nodes = [
    [0, 1, 4],
    [1, 2, 3],
    [2, -1, -1],
    [3, -1, -1],
    [4, 5, 8],
    [5, 6, 7],
    [6, -1, -1],
    [7, -1, -1],
    [8, -1, -1]
]

binary_tree_info(n, nodes)