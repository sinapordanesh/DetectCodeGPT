S=input()
N=len(S)
mod= 998244353

FACT=[1]
for i in range(1,2*10**5+1):
    FACT.append(FACT[-1]*i%mod)

FACT_INV=[pow(FACT[-1],mod-2,mod)]
for i in range(2*10**5,0,-1):
    FACT_INV.append(FACT_INV[-1]*i%mod)

FACT_INV.reverse()

def Combi(a,b):
    if 0<=b<=a:
        return FACT[a]*FACT_INV[b]*FACT_INV[a-b]%mod
    else:
        return 0

R=0
B=0

RB=[[0,0]]*N

for i in range(N):
    s=S[i]
    if s=="0":
        R+=2
    elif s=="1":
        R+=1
        B+=1
    else:
        B+=2
    RB[i]=[R,B]

DP=[0]*(R+1)
DP[0]=1

for i in range(N):
    NDP=[0]*(R+1)
    red,blue=RB[i]
    for r in range(R+1):
        if DP[r]==0:
            continue
        if r+1<=red:
            NDP[r+1]+=DP[r]
        if i-r+1<=blue:
            NDP[r]+=DP[r]
    DP=NDP


ANS=0
for r in range(R+1):
    red=R-r
    blue=B-(N-r)

    ANS=ANS+DP[r]*Combi(red+blue,blue)
    ANS%=mod
print(ANS)