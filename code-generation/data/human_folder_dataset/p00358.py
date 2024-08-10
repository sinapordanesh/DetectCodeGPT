import sys
sys.setrecursionlimit(10**6)
H, N = map(int, input().split())
P = [0]*H
for i in range(N):
    x, y = map(int, input().split())
    P[y] |= 1 << x

memo = [[-1]*16 for i in range(H)]
for i in range(16):
    memo[H-1][i] = 0
def dfs(i, state):
    if memo[i][state] != -1:
        return memo[i][state]
    p = P[i+1]
    s = state | p
    r = dfs(i+1, p)
    if s & 0b0011 == 0:
        r = max(r, dfs(i+1, p | 0b0011) + 1)
    if s & 0b0110 == 0:
        r = max(r, dfs(i+1, p | 0b0110) + 1)
    if s & 0b1100 == 0:
        r = max(r, dfs(i+1, p | 0b1100) + 1)
    if s & 0b1111 == 0:
        r = max(r, dfs(i+1, 0b1111) + 2)
    memo[i][state] = r
    return r
print(dfs(0, P[0]))
