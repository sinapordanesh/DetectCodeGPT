import sys
readline = sys.stdin.buffer.readline

def make_modinv_list(n, mod=10**9+7):
    inv_list = [0]*(n+1)
    inv_list[1] = 1
    for i in range(2, n+1):
        inv_list[i] = (mod - mod//i * inv_list[mod%i] % mod)
    return inv_list

mod = 998244353
N = int(readline())
A = list(map(int, readline().split()))
C = max(A) + 1
inv_list = make_modinv_list(C, mod)
h = [0] * C
for x in A:
    h[x] = (h[x] + x) % mod
for i in range(1, C):
    for j in range(i*2, C, i):
        h[i] = (h[i] + h[j]) % mod
g = [0] * C
for i in range(1, C):
    g[i] = h[i] * h[i] % mod
for i in range(C-1, 0, -1):
    for j in range(i*2, C, i):
        g[i] = (g[i] - g[j]) % mod
ans = 0
for i in range(1, C):
    ans = (ans + g[i] * inv_list[i]) % mod
ans -= sum(A)
print(ans * inv_list[2] % mod)    
