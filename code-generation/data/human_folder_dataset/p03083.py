b,w=map(int,input().split())
dp=[0]*(b+w)
dp[0]=1/2
mod=pow(10,9)+7

def cmb(n,r,mod):
  if (r<0 or r>n):
    return 0
  r=min(r,n-r)
  return g1[n]*g2[r]*g2[n-r]%mod
g1=[1,1] # g1[i]=i! % mod　:階乗
g2=[1,1] # g2[i]=(i!)^(-1) % mod　:階乗の逆元
inverse=[0,1]
for i in range(2,b+w+1):
  g1.append((g1[-1]*i)%mod)
  inverse.append((-inverse[mod%i]*(mod//i))%mod)
  g2.append((g2[-1]*inverse[-1])%mod)
t1,t2=0,0
for i in range(1,1+b+w):
  t=pow(2,mod-2,mod)
  if i-b>0:
    t1*=2
    t1%=mod
    t1+=cmb(i-2,b-1,mod)
    t1%=mod
    tmp=t1*pow(2,mod-1-i,mod)
    tmp%=mod
    t-=tmp
    t%=mod
  if i-w>0:
    t2*=2
    t2%=mod
    t2+=cmb(i-2,w-1,mod)
    t2%=mod
    tmp=t2*pow(2,mod-1-i,mod)
    tmp%=mod
    t+=tmp
    t%=mod
  print(t)

