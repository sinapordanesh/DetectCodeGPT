N, M = map(int, input().split())
mod = 10**9 + 7

def factorial(n):
    ans = 1
    i = 0
    while i < n:
        ans *= (n-i)
        ans %= mod
        i += 1
    return ans

if abs(N-M) >= 2:
    print(0)
elif N == M:
    ans = (factorial(N) * factorial(M) * 2) % mod
    print(ans)
else:
    ans = (factorial(N) * factorial(M)) % mod
    print(ans)
