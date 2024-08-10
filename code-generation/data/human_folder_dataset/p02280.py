def search(ps, id):
    if ps[id] == -1:
        return 0
    else:
        return 1 + search(ps, ps[id])


def search_part2(tree, id):
    if tree[id][0] == -1:
        left = -1
    else:
        left = search_part2(tree, tree[id][0])

    if tree[id][1] == -1:
        right = -1
    else:
        right = search_part2(tree, tree[id][1])

    return 1 + max(left, right)


n = int(input())
tree = [[] for _ in range(n)]
ps = [-1 for _ in range(n)]
ss = [-1 for _ in range(n)]

for _ in range(n):
    s = input().split()
    id = int(s[0])
    left = int(s[1])
    right = int(s[2])
    tree[id] = [left, right]
    if left >= 0:
        ps[left] = id
        ss[left] = right
    if right >= 0:
        ps[right] = id
        ss[right] = left

for id in range(n):
    p = ps[id]
    s = ss[id]
    deg = int(tree[id][0] >= 0) + int(tree[id][1] >= 0)
    d = search(ps, id)
    h = search_part2(tree, id)

    if p == -1:
        type = "root"
    elif tree[id][0] == -1 and tree[id][1] == -1:
        type = "leaf"
    else:
        type = "internal node"

    print("node " + str(id) + ": parent = " + str(p) + ", sibling = " + str(s) + ", degree = " + str(
        deg) + ", depth = " + str(d) + ", height = " + str(h) + ", " + type)

