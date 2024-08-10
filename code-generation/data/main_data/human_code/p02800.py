import sys
input = sys.stdin.readline

H,W=map(int,input().split())
A=[input().strip() for i in range(H)]

mod=998244353

# factorial,facotiralの逆数を事前計算.
FACT=[1]
for i in range(1,21):
    FACT.append(FACT[-1]*i%mod)

FACT_INV=[pow(FACT[-1],mod-2,mod)]
for i in range(20,0,-1):
    FACT_INV.append(FACT_INV[-1]*i%mod)

FACT_INV.reverse()

COMBI=[[-1]*21 for i in range(21)]
def Combi(a,b):
    if COMBI[a][b]!=-1:
        return COMBI[a][b]
    
    if 0<=b<=a:
        COMBI[a][b]=FACT[a]*FACT_INV[b]*FACT_INV[a-b]%mod
        return COMBI[a][b]
    else:
        COMBI[a][b]=0
        return 0

M=max(H,W)+1
RA=[[-1]*M for i in range(M)]
def rect(H,W):
    if H==W==0:
        return 1
    if RA[H][W]!=-1:
        return RA[H][W]
    
    DP=[[[0,0] for j in range(W+1)] for i in range(H+1)] # (h,w)の最後に進んだ向きが縦/横のときの場合の数
    DP[0][0][0]=1
    DP[0][0][1]=1

    for h in range(H+1):
        for w in range(W+1):
            for nexth in range(h+1,H+1):
                DP[nexth][w][0]+=DP[h][w][1]*FACT_INV[nexth-h]
                DP[nexth][w][0]%=mod

            for nextw in range(w+1,W+1):
                DP[h][nextw][1]+=DP[h][w][0]*FACT_INV[nextw-w]
                DP[h][nextw][1]%=mod

    RA[H][W]=RA[W][H]=sum(DP[H][W])%mod*FACT[H]*FACT[W]%mod

    return RA[H][W]

CA=[[-1]*(W+1) for i in range(H+1)]
def calc(h,w):
    if CA[h][w]!=-1:
        return CA[h][w]
    
    RET=0
    
    for bh in range(h+1):
        for bw in range(w+1):
            RET+=rect(bh,w-bw)*rect(h-bh,bw)*Combi(h,bh)*Combi(w,bw)
            #print(bh,bw,w-bw,h-bh,rect(bh,w-bw),rect(h-bh,bw),Combi(h,bh),Combi(w,bw))
            RET%=mod

    CA[h][w]=RET%mod
    return CA[h][w]

for i in range(H+1):
    for j in range(W+1):
        calc(i,j)

ANS=rect(H,W)

for i in range((1<<H)-1):
    for j in range((1<<W)-1):
        okflag=1
        for h in range(H):
            if i & (1<<h)!=0:
                continue
            coinc=""
            dif=0
            for w in range(W):
                if j & (1<<w)!=0:
                    continue

                if coinc=="":
                    coinc=A[h][w]
                elif A[h][w]!=coinc:
                    dif=1
                    break

            if dif==0:
                okflag=0
                break

        if okflag==0:
            continue

        okflag=1
        for w in range(W):
            if j & (1<<w)!=0:
                continue
            coinc=""
            dif=0
            for h in range(H):
                if i & (1<<h)!=0:
                    continue

                if coinc=="":
                    coinc=A[h][w]
                elif A[h][w]!=coinc:
                    dif=1
                    break
                
            if dif==0:
                okflag=0
                break

        if okflag==0:
            continue

        # i, jのうち、0の部分は決定済み. 1の部分に自由度がある.
        HR=WR=0
        for h in range(H):
            if i & (1<<h)!=0:
                HR+=1
        for w in range(W):
            if j & (1<<w)!=0:
                WR+=1

        ANS+=CA[HR][WR]
            
        #ANS%=mod

        
print(ANS%mod)