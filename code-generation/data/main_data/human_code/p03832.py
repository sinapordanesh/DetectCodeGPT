import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,a,b,c,d = list(map(int, input().split()))
dp = [0]*(n+1)
dp[0] = 1
M = 10**9+7
### 素数の逆元とCombination
N = n+10 # 必要なテーブルサイズ

g1 = [None] * (N+1) # 元テーブル
g2 = [None] * (N+1) #逆元テーブル
inverse = [None] * (N+1) #逆元テーブル計算用テーブル
g1[0] = g1[1] = g2[0] = g2[1] = 1
inverse[0], inverse[1] = [0, 1] 

for i in range( 2, N + 1 ):
    g1[i] = ( g1[i-1] * i ) % M 
    inverse[i] = ( -inverse[M % i] * (M//i) ) % M # ai+b==0 mod M <=> i==-b*a^(-1) <=> i^(-1)==-b^(-1)*aより
    g2[i] = (g2[i-1] * inverse[i]) % M 

def cmb(n, r, M):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return (g1[n] * g2[r] * g2[n-r]) % M

for i in range(a, b+1):
    for j in range(n, 0, -1):
        val = 1
        for k in range(c):
            val *= cmb(j-i*k, i, M)
            val %= M
        for k in range(c,d+1):
            if j-i*k>=0:
                dp[j] += dp[j-i*k] * val * g2[k]
                dp[j] %= M
                val *= (cmb(j-i*k, i, M))
                val %= M
            else:
                break
#     print(dp)
print(dp[n]%M)