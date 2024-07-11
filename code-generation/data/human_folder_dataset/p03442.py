N = int(input())
B = [0]*N
for i in range(N-1):
    x, y, a = map(int, input().split())
    B[x] ^= a
    B[y] ^= a
D = {}
for b in B:
    D[b] = D.get(b, 0) + 1
D[0] = 0
ans = 0
first = 0
for b in D:
    ans += D[b]//2
    if D[b]%2:
        first |= 1 << b

A = [0]*(1 << 16)
for i in range(1, 1<<16):
    bit = i & -i
    l = len(bin(bit))-3
    A[i] = A[i ^ bit] ^ l

memo = {0: 0}
def dfs(state):
    if state in memo:
        return memo[state]
    cur = state
    res = 10**9+7
    while cur:
        if A[cur] == 0:
            res = min(res, dfs(state ^ cur) + bin(cur).count('1')-1)
        cur -= 1
        cur &= state
    memo[state] = res
    return res
ans += dfs(first)
print(ans)
