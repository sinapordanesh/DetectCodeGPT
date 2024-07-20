import sys

from bisect import bisect_left
from collections import defaultdict
from itertools import accumulate


class UnionFind:
    def __init__(self, n):
        self.table = [-1] * n

    def _root(self, x):
        stack = []
        tbl = self.table
        while tbl[x] >= 0:
            stack.append(x)
            x = tbl[x]
        for y in stack:
            tbl[y] = x
        return x

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def unite(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1

    def get_size(self, x):
        return -self.table[self._root(x)]


def solve():
    n, m = map(int, sys.stdin.buffer.readline().split())

    extra_durabilities = [0] * n
    self_loop_durabilities = [[] for _ in range(n)]
    outdegrees = [0] * n
    base_operation_count = 0
    uft = UnionFind(n)

    mp = map(int, sys.stdin.buffer.read().split())
    for a, b, c in zip(mp, mp, mp):
        a -= 1
        b -= 1
        outdegrees[a] += 1
        if a == b:
            if c >= 2:
                self_loop_durabilities[a].append(c)
            continue
        uft.unite(a, b)
        extra_durabilities[a] += c - 1
        base_operation_count += 1

    # components[root] = [size, max_outdegree, durability(non-self-loop), self-loop-durability]
    components = defaultdict(lambda: [0, 0, 0, []])
    for i in range(n):
        r = uft._root(i)
        item = components[r]
        item[0] += 1
        item[1] = max(item[1], outdegrees[i])
        item[2] += extra_durabilities[i]
        item[3].extend(self_loop_durabilities[i])

    exists_initial_catalyst_on_moving_path = False
    exists_initial_catalyst_at_self_loop = False
    supplied_catalyst = 0
    demanded_catalyst = 0
    self_loop_catalysts_cost1 = []
    self_loop_catalysts_cost2 = []

    for i, (cnt, deg, dur, sel) in components.items():
        if cnt == 1:
            if deg == 1:
                self_loop_catalysts_cost2.extend(c - 2 for c in sel)
            else:
                if len(sel) >= 1:
                    self_loop_catalysts_cost1.extend(c - 1 for c in sel)
                    exists_initial_catalyst_at_self_loop = True
            continue
        if deg == 1:
            supplied_catalyst += dur
            demanded_catalyst += 1
        else:
            supplied_catalyst += dur
            if dur >= 1:
                exists_initial_catalyst_on_moving_path = True
            elif len(sel) >= 1:
                exists_initial_catalyst_at_self_loop = True
        self_loop_catalysts_cost1.extend(c - 1 for c in sel)

    # print(base_operation_count, supplied_catalyst, demanded_catalyst,
    #       exists_initial_catalyst_on_moving_path, exists_initial_catalyst_at_self_loop)

    if demanded_catalyst == 0:
        return base_operation_count

    if not exists_initial_catalyst_on_moving_path and not exists_initial_catalyst_at_self_loop:
        return -1

    if supplied_catalyst >= demanded_catalyst:
        if exists_initial_catalyst_on_moving_path:
            return base_operation_count + demanded_catalyst
        else:
            return base_operation_count + demanded_catalyst + 1

    self_loop_catalysts_cost1.sort(reverse=True)
    self_loop_catalysts_cost2.sort(reverse=True)
    # print(self_loop_catalysts_cost1)
    # print(self_loop_catalysts_cost2)
    acc1 = [0] + list(accumulate(self_loop_catalysts_cost1))
    acc2 = [0] + list(accumulate(self_loop_catalysts_cost2))
    # print(acc1)
    # print(acc2)
    shortage = demanded_catalyst - supplied_catalyst
    if acc1[-1] + acc2[-1] < shortage:
        return -1

    cost = 10 ** 18
    for use1 in range(0 if exists_initial_catalyst_on_moving_path else 1, len(acc1)):
        cat = acc1[use1]
        remaining = shortage - cat
        if remaining <= 0:
            cost = min(cost, use1)
            break
        if remaining > acc2[-1]:
            continue
        use2 = bisect_left(acc2, remaining)
        cost = min(cost, use1 + 2 * use2)

    return base_operation_count + demanded_catalyst + cost


print(solve())
