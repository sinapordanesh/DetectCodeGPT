import sys
def I(): return int(sys.stdin.readline().rstrip())


N = I()
mod = 10**9+7


fac = [1]*(N+1)
for i in range(1,N+1):
    fac[i] = (fac[i-1]*i) % mod

fac_inverse = [1]*(N+1)
for i in range(1,N+1):
    fac_inverse[i] = pow(fac[i],mod-2,mod)


def nCr(n,r):
    if n < r:
        return 0
    return (fac[n]*fac_inverse[r]*fac_inverse[n-r]) % mod


A = [0]*(N+1)  # Ai = i回以下マシンを稼働することで、全て黒く塗られるような順列の個数
for i in range(N+1):
    A[i] = (fac[i]*fac[N-1-i]*nCr(i-1,N-1-i)) % mod

ans = 0
for i in range(1,N):
    ans += i*(A[i]-A[i-1])
    ans %= mod

print(ans)
