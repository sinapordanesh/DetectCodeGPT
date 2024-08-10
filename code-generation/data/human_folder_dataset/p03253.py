from collections import Counter

N,M=map(int,input().split())
mod = 10**9+7

factorial=[1 for i in range(10**6)]
for i in range(2,10**6):
    factorial[i] = factorial[i-1]*i % mod

def comb(n,k):
    return (factorial[n]*pow(factorial[n-k]*factorial[k], -1, mod))%mod

def factorize(n):
    out=[]
    i = 2
    while 1:
        if n%i==0:
            out.append(i)
            n //= i
        else:
            i += 1
        if n == 1:break
        if i > int(n**.5+3):
            out.append(n)
            break
    
    return out
  
c = Counter(factorize(M))

ans = 1
for k in c.keys():
  ans *= comb(c[k]+N-1,N-1)
  ans %= mod
  
print(ans)