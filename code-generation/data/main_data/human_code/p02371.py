import sys
sys.setrecursionlimit(10**6)

N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    s, t, w = map(int, input().split())
    G[s].append([t, w])
    G[t].append([s, w])


def dfs(n):
    visited = [False] * N
    stack = [[n, 0]]
    longest = [-1, -1]

    while stack:
        node, weight = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        if longest[1] < weight:
            longest = [node, weight]

        for n, w in G[node]:
            if not visited[n]:
                stack.append([n, w + weight])

    return longest


xn, xw = dfs(0)
yn, yw = dfs(xn)
print(yw)

