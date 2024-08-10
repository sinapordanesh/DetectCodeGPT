def blackboard_sum(N, X, S):
    MOD = 10**9 + 7
    ans = 0
    
    def mod(x, y):
        return x % y
    
    def rec(idx, x):
        nonlocal ans
        if idx == N:
            ans = (ans + x) % MOD
            return
        rec(idx + 1, mod(x, S[idx]))
        rec(idx + 1, x)
    
    rec(0, X)
    
    return ans

N, X, *S = map(int, input().split())
print(blackboard_sum(N, X, S))