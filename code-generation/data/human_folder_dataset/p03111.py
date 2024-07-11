N, A, B, C = map(int, input().split())
l = [int(input()) for i in range(N)]
 
INF = float('inf')
ans = INF
 
def dfs(a, b, c, n, cost):
    global ans
    if n == N:
        cost += abs(A - a) + abs(B - b) + abs(C - c) - 30 if min(a, b, c) > 0 else INF
        ans = min(ans, cost)
        return
    dfs(a, b, c, n+1, cost)
    dfs(a+l[n], b, c, n+1, cost+10)
    dfs(a, b+l[n], c, n+1, cost+10)
    dfs(a, b, c+l[n], n+1, cost+10)
 
dfs(0, 0, 0, 0, 0)
print(ans)
