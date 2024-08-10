import sys
from operator import sub

sys.setrecursionlimit(100000)


def dfs(s, visited):
    visited.add(s)
    for v in links[s]:
        if v not in visited:
            dfs(v, visited)


def solve():
    checked = set()
    for i in range(ls // 2 + 1):
        if i in checked:
            continue
        visited = set()
        dfs(i, visited)
        inner_total = sum(sd[k] for k in visited) % 26
        if inner_total != 0:
            return False
        checked.update(visited)
    return True


s = input()
sl = list(map(ord, s))
sd = list(map(sub, sl + [97], [97] + sl))
ls = len(s)
lsd = len(sd)

n = int(input())
links = [set() for _ in range(lsd)]

for i in range((ls + 1) // 2):
    links[i].add(ls - i)
    links[ls - i].add(i)
for a, b in (map(int, input().split()) for _ in range(n)):
    links[a - 1].add(b)
    links[b].add(a - 1)

print('YES' if solve() else 'NO')
