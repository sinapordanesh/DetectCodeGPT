import sys
input = sys.stdin.readline

U = 4*10**6
MOD = 998244353
 
fact = [1]*(U+1)
fact_inv = [1]*(U+1)
 
for i in range(1,U+1):
    fact[i] = (fact[i-1]*i)%MOD
fact_inv[U] = pow(fact[U], MOD-2, MOD)
 
for i in range(U,0,-1):
    fact_inv[i-1] = (fact_inv[i]*i)%MOD
 
def perm(n, k):
    if k < 0 or k > n:
        return 0
    z = fact[n]
    z *= fact_inv[n-k]
    z %= MOD
    return z

def comb(n, k):
    if k < 0 or k > n:
        return 0
    z = fact[n]
    z *= fact_inv[k]
    z %= MOD
    z *= fact_inv[n-k]
    z %= MOD
    return z

n, m = map(int, input().split())
ans = 0
for k in range(m%2, min(n, m)+1, 2):
  ans += comb((3*m-k)//2+n-1, n-1) * comb(n, k)
  ans %= MOD
cnt = 0
for k in range(m):
  cnt += comb(k+n-2, n-2)
  cnt %= MOD
cnt *= n
cnt %= MOD
ans -= cnt
ans %= MOD
print(ans)