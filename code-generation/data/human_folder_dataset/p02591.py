#import random,time

H=int(input())
#P=[i for i in range(2**(H-1))]
#random.shuffle(P)
P=list(map(lambda x:int(x)-1,input().split()))
mod=10**9+7
inv=pow(2,mod-2,mod)

L=2**(H-1)

base_t=[1 for i in range(1+1<<H)]
base_t[0]=0
for i in range(2,1+1<<H):
    base_t[i]=i*base_t[i>>1]
    base_t[i]%=mod

base_s=[(i*pow(base_t[i]**2,mod-2,mod))%mod for i in range(1+1<<H)]

ans=0
def solve(i):
    global ans
    if i>=L:
        i-=L
        val=(base_t[i+L]*base_t[P[i]+L])%mod
        val2=pow(val,2,mod)
        id=P[i]+L
        res=[[(P[i]+L)>>(H-1-j),val,val2] for j in range(H)]
        return res
    L1=solve(2*i)
    L2=solve(2*i+1)
    Li,ttt=merge(L1,L2)
    ttt=(ttt*(base_s[i]-base_s[i>>1]))%mod
    ans=(ans+ttt)%mod
    return Li

def merge(L1,L2):
    res=[]
    L1.append([10**18,0])
    L2.append([10**18,0])
    L1=L1[::-1]
    L2=L2[::-1]
    ttt=0
    if L1[-1][0]<=L2[-1][0]:
        res.append(L1.pop())
    else:
        res.append(L2.pop())
    while L1 and L2:
        if L1[-1][0]<=L2[-1][0]:
            if res and res[-1][0]==L1[-1][0]:
                res[-1][1]+=L1[-1][1]
                res[-1][1]%=mod
                res[-1][2]+=L1[-1][2]
                res[-1][2]%=mod
                L1.pop()
            else:
                j,val,val2=res[-1]
                tmp=(base_s[j]-base_s[j>>1]) %mod
                c=val**2 %mod
                c=(c-val2)%mod
                tmp =(tmp*c) %mod
                ttt=(ttt+tmp)%mod
                res.append(L1.pop())
        else:
            if res and res[-1][0]==L2[-1][0]:
                res[-1][1]+=L2[-1][1]
                res[-1][1]%=mod
                res[-1][2]+=L2[-1][2]
                res[-1][2]%=mod
                L2.pop()
            else:
                j,val,val2=res[-1]
                tmp=(base_s[j]-base_s[j>>1]) %mod
                c=val**2 %mod
                c=(c-val2)%mod
                tmp =(tmp*c) %mod
                ttt=(ttt+tmp)%mod
                res.append(L2.pop())
    res.pop()
    return res,ttt

solve(1)

print(ans*inv %mod)
