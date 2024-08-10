# doc: git.io/vy4co
def graph(inp):
    nodes = dict()
    N = None
    for line in inp.splitlines():
        if N is None:
            N = int(line.strip())
            for k in range(1, N + 1):
                nodes[k] = set()
            continue
        i, k = map(int, line.split())
        nodes[i].add(k)
        nodes[k].add(i)
    return nodes

def trace(nodes, start, exclude=None):
    return (start,) + max([trace(nodes, n, exclude=start) for n in nodes[start] if n != exclude], key=len, default=())

def tree(nodes, start, exclude=None):
    return tup([tree(nodes, n, exclude=start) for n in nodes[start] if n != exclude])

class tup(tuple):
    def __new__(cls, arg=()):
        rv = super().__new__(cls, arg)
        rv.height = (1 + min((t.height[0] for t in rv), default=-1),
                     1 + max((t.height[1] for t in rv), default=-1))
        rv.edges = len(rv) + sum(t.edges for t in rv)
        return rv

def combinations(nodes):
    path = trace(nodes, trace(nodes, next(iter(nodes)))[-1])
    D = len(path)
    C = D // 2
    root = path[D // 2]
    if D % 2:
        thetree = tree(nodes, root)
        return sum(enum(limits, thetree) for limits in zip(range(C + 1), reversed(range(C + 1))))
    else:
        left = path[D // 2 - 1]
        left_tree = tup([tree(nodes, left, exclude=root)])
        right_tree = tree(nodes, root, exclude=left)
        lg = [i // 2 for i in range(1, C * 2 + 2)]
        ll = list(zip(lg, reversed(lg)))
        rg = [i // 2 for i in range(C * 2 + 1)]
        rl = list(zip(rg, reversed(rg)))
        tot = 0
        for i in range(len(ll)):
            left_limits = ll[i]
            right_limits = rl[i]
            lrv = enum(left_limits, left_tree) - sum(enum(ne, left_tree) for ne in ll[i - 1: i] + ll[i + 1: i + 2])\
                if sum(left_limits) > C else enum(left_limits, left_tree)
            rrv = enum(right_limits, right_tree)
            tot += lrv * rrv
        return tot

def enum(limits, shape, _cache=dict()):
    limits = tuple(sorted(limits))
    r, b = limits
    low, high = shape.height

    if r >= high:
        return 2 ** shape.edges

    if 0 in limits:
        return 1

    key = hash((r, b, shape))
    if key not in _cache:
        tot = 1
        for subtree in shape:
            acc = 0
            for sublimit in ((r - 1, b), (r, b - 1)):
                acc += enum(sublimit, subtree)
            tot *= acc
        _cache[key] = tot
    return _cache[key]

import sys
sys.setrecursionlimit(99999)
g = graph(sys.stdin.read())
rv = combinations(g)
print(rv % (10 ** 9 + 7))