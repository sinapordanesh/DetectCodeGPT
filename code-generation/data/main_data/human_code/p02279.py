N = int(input())

def get_parent(node):
    parent = -1
    if "parent" in node:
        parent = node["parent"]
    return parent

def get_depth(node):
    depth = 0
    while "parent" in node:
        depth += 1
        parent = node["parent"]
        node = rooted_tree[parent]
    return depth

def get_node_type(node):
    if "parent" not in node:
        return "root"
    if "left" not in node:
        return "leaf"
    return "internal node"

def get_children(node):
    if "left" not in node:
        return "[]"
    left = node["left"]
    siblings = []
    siblings.append(str(left))
    while rooted_tree[left]["right"] > -1:
        right = rooted_tree[left]["right"]
        siblings.append(str(right))
        left = right
    return "[{}]".format(", ".join(siblings))

rooted_tree = [{} for i in range(N)]
for _ in range(N):
    row = input()
    id, degree, *children = list(map(int, row.split()))
    if degree > 0:
        rooted_tree[id]["left"] = children[0]
        for i in range(len(children)):
            child_id = children[i]
            right = -1
            if i < len(children)-1:
                right = children[i+1]
            rooted_tree[child_id]["right"] = right
            rooted_tree[child_id]["parent"] = id

for id in range(N):
    node = rooted_tree[id]
    parent = get_parent(node)
    depth = get_depth(node)
    node_type = get_node_type(node)
    children = get_children(node)
    print("node {}: parent = {}, depth = {}, {}, {}".format(id, parent, depth, node_type, children))
