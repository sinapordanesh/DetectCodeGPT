import sys

from itertools import combinations


def solve(n, pairs):
    survivors = {v: {v} for v in range(1, n + 1)}
    for x, y in reversed(pairs):
        for v, srv in survivors.copy().items():
            if x in srv:
                if y in srv:
                    del survivors[v]
                else:
                    srv.add(y)
            elif y in srv:
                srv.add(x)
    return sum(su.isdisjoint(sv) for su, sv in combinations(survivors.values(), 2))


n, m = map(int, input().split())
pairs = [tuple(map(int, line.split())) for line in sys.stdin.readlines()]
print(solve(n, pairs))
