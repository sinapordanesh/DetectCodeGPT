MOD = 998244353

def solve(N, M, squares):
    ans = 1
    for i in range(1, N+1):
        ans = (ans * 2) % MOD
    return ans

N, M = map(int, input().split())
squares = [list(map(int, input().split())) for _ in range(M)]

print(solve(N, M, squares))