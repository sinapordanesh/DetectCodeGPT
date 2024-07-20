
"""

https://atcoder.jp/contests/agc009/tasks/agc009_c

A <= B としてよい
dpだろうなぁ

dpA[i][X] = 1つ前を置いたのがBで、Aに置かれた最大がindexXの時の置き方
dpB[i][X] = 同様

if S[i]-S[i-1] >= B:
    dpA[i][X] = dpA[i-1][X]
    if X == i-1:
        dpA[i][X] = ///


推移は、BITですればおｋ

もし差がB以下ならば→直前にBを置いていた場所に重ねおきはできない
→直前にAに置いていて、なおかつ最後にBに置いたのとの差がB以下の場合だけBにおける
→dpA[i][i-1]以外は0になる

#直前とB以上の差があるとき
if X != i-1:
    dpBに置く[i][最後にAに置いたのがX] = dpB[i-1][X]
else:
    dpB[i][i-1] = ΣdpA[i-1][y] (y<=S-B)
#差がないとき
if X == i-1:
    dpB[i][i-1] = ΣdpA[i-1][y] (y<=S-B)
else:
    dpB[i][X] = 0

"""

import sys
from sys import stdin
from collections import deque

def bitadd(a,w,bit): #aにwを加える(1-origin)
 
    x = a
    while x <= (len(bit)-1):
        bit[x] += w
        x += x & (-1 * x)
 
def bitsum(a,bit): #ind 1～aまでの和を求める
 
    ret = 0
    x = a
    while x > 0:
        ret += bit[x]
        x -= x & (-1 * x)
    return ret

N,A,B = map(int,stdin.readline().split())
mod = 10**9+7

BITA = [0] * (N+3)
BITB = [0] * (N+3)
bitadd(1,1,BITA)
#bitadd(0,1,BITB)

aq = deque([])
bq = deque([])
Slis = [float("-inf")]

for loop in range(N):

    S = int(stdin.readline())
    
    aq.append( (S,loop+2) )
    bq.append( (S,loop+2) )
    while aq[0][0] <= S-A:
        aq.popleft()
    while bq[0][0] <= S-B:
        bq.popleft()

    #dpAへの推移(Bに置く)
    #Bに置けるのは、1つ前との差がB以上の場合全部おk
    #そうでない場合、前にAにおいていて、かつ差がB以上の場合

    """
    #全てokの場合
    if S - Slis[-1] >= B:
        Aans = bitsum(bq[0][1]-1,BITB)
        Aans %= mod
    else: #そうでない場合→直前にAに置いていた場合のみ可能→bitをリセットする必要あり
        Aans = bitsum(bq[0][1]-1,BITB)
        Aans %= mod

    if S - Slis[-1] >= A:
        Bans = bitsum(aq[0][1]-1,BITA)
        Bans %= mod
    else:
        Bans = bitsum(aq[0][1]-1,BITA)
        Bans %= mod
    """
    Aans = bitsum(bq[0][1]-1,BITB)
    Bans = bitsum(aq[0][1]-1,BITA)
    
    if Aans < 0:
        Aans = 0
    if Bans < 0:
        Bans = 0

    Aans %= mod
    Bans %= mod

    #print (Aans,Bans)
    #更新
    if S - Slis[-1] >= B:
        bitadd(loop+1,Aans,BITA)
    else:
        nowsum = bitsum(N+2,BITA)
        bitadd(1,-1*nowsum,BITA)
        bitadd(loop+1,Aans,BITA)

    if S - Slis[-1] >= A:
        bitadd(loop+1,Bans,BITB)
    else:
        nowsum = bitsum(N+2,BITB)
        bitadd(1,-1*nowsum,BITB)
        bitadd(loop+1,Bans,BITB)

    Slis.append(S)
    if len(Slis) >= 3 and Slis[-1] - Slis[-3] < min(A,B):
        print (0)
        sys.exit()

print ((bitsum(N+2,BITA) + bitsum(N+2,BITB))% mod)
    
        
    
