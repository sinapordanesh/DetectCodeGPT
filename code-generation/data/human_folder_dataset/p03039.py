N, M, K = map(int, input().split())
mod = 10**9+7

def nCk(n, k, mod):
    nu = 1
    de = 1 
    for i in range(1, k+1):
        nu *= (n-i+1)
        de *= i
        nu = nu % mod
        de = de % mod
    ans = nu * pow(de, mod-2, mod) % mod
    return ans

ans = nCk(N*M-2, K-2, mod)*N*M*(M+N)*(M*N-1)//6
ans = ans % mod
print(ans)