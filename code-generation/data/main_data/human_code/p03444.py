from collections import deque


def get_children(ps):
    children = [set() for _ in range(n)]
    for i, p in enumerate(ps):
        children[p].add(i + 1)
    return children


def make_levels(cs):
    levels_set = []
    levels_dict = {}
    queue = deque([(0, 0)])
    while queue:
        i, l = queue.popleft()
        if fixed[i]:
            continue
        if len(levels_set) <= l:
            levels_set.append(set())
        levels_set[l].add(i)
        levels_dict[i] = l
        queue.extend((c, l + 1) for c in cs[i])
    return levels_set, levels_dict


def make_where(aa):
    where = [0] * n
    for i, a in enumerate(aa):
        where[a] = i
    return where


def get_leaves(levels):
    leaves = {}
    children_count = [-1] * n
    for l, cs in reversed(list(enumerate(levels))):
        for c in cs:
            cc = children_count[c]
            pi = ps[c - 1]
            if cc == -2:
                children_count[pi] = -2
                continue

            if cc == -1:
                if aa[c] == c:
                    fixed[c] = True
                    continue
                leaves[c] = c
                cc = c
            else:
                leaves[c] = cc

            if children_count[pi] == -1:
                children_count[pi] = cc
            else:
                children_count[pi] = -2
    return leaves


def put(i, x):
    buf.append(i)
    where[x] = i
    x, aa[i] = aa[i], x
    while i:
        pi = ps[i - 1]
        where[x] = pi
        x, aa[pi] = aa[pi], x
        i = pi


def solve():
    cs = get_children(ps)
    levels_set, levels_dict = make_levels(cs)
    while not fixed[0]:
        leaves = get_leaves(levels_set)
        while leaves:
            root = aa[0]
            if root in leaves:
                gci = leaves[root]
                while True:
                    a = aa[gci]
                    if not fixed[a] or a < root:
                        put(gci, root)
                        fixed[root] = True
                        break
                    gci = ps[gci - 1]
                del leaves[root]
            else:
                ml, mi = max((levels_dict[where[i]], where[i]) for i in leaves)
                put(mi, root)


n = int(input())
ps = list(map(int, input().split()))
aa = list(map(int, input().split()))
where = make_where(aa)
fixed = [False] * n
buf = []
solve()
print(len(buf))
print('\n'.join(map(str, buf)))
