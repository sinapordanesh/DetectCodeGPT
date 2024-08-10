def cmb(n, r, mod):#コンビネーションの高速計算　
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**5
g1 = [1]*(N+1) # 元テーブル
g2 = [1]*(N+1) #逆元テーブル
inverse = [1]*(N+1) #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1[i]=( ( g1[i-1] * i ) % mod )
    inverse[i]=( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2[i]=( (g2[i-1] * inverse[i]) % mod )
inverse[0]=0

N,M=map(int,input().split())
A=[0]+list(map(int,input().split()))
dp=[[0 for i in range(2**N)] for j in range(M+1)]

dp[0][0]=g1[2**N-1]

for i in range(1,M+1):
    for j in range(2**N):
        dp[i][j]=dp[i-1][j]
        for k in range(N):
            if j>>k &1==0 and 2**N-A[i]-j>=2**k-1:
                dp[i][j]=(dp[i][j]+((-1)*((g1[2**N-A[i]-j]*g2[2**N-A[i]+1-(j+2**k)])%mod)*((dp[i-1][j+2**k]+g1[2**N-1-j-2**k])*2**k)%mod)%mod)%mod

#for i in range(M+1):
    #print(dp[i])
print((dp[M][0]*pow(2,N,mod))%mod)
