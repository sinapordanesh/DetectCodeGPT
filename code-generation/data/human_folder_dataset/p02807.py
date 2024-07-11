n=int(input())
x=list(map(int,input().split()))
mod=10**9+7

# コンビネーション、さらに高速。あらかじめO(N)の計算をすることでのちの計算が早くなる
def cmb(n,r,mod):
  if (r<0 or r>n):
    return 0
  r=min(r,n-r)
  return g1[n]*g2[r]*g2[n-r]%mod
g1=[1,1] # g1[i]=i! % mod　:階乗
g2=[1,1] # g2[i]=(i!)^(-1) % mod　:階乗の逆元
inverse=[0,1]
for i in range(2,n+1):
  g1.append((g1[-1]*i)%mod)
  inverse.append((-inverse[mod%i]*(mod//i))%mod)
  g2.append((g2[-1]*inverse[-1])%mod)

ans=0
nn=[g1[n-1]]
tmp=g1[n-1]
for i in range(2,n):
  tmp+=g1[n-1]*pow(i,mod-2,mod)
  tmp%=mod
  nn.append(tmp)
  
for i in range(n-1):
  d=x[i+1]-x[i]
  ans+=d*nn[i]
  ans%=mod
print(ans)
