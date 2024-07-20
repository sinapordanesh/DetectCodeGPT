
"""

https://atcoder.jp/contests/arc083/tasks/arc083_c

NもXも小さい→重みで場合分けできる？
白と黒は、片方が重み0でなくてはいけないという制約以外は独立
木dpを考える

dp[v][black][white] = vの子部分木の重みの和がそれぞれblとwhの時の割り当てが可能か
→bitsetとかも思いつくが、blかwhはX[i]になることを利用して計算量を削減する

重みは根のほうでいくらでも大きくできるが、小さくはできないことに注目

dp[v][color] = 頂点vをcolorにした場合の、colorでない頂点の合計の最小値
dp[v][black] を求めたい。黒にするためには、黒の合計がXi以下でなくてはならない
→それぞれの子から2通りの bl,whをもらう。うまく組み合わせて、blがXi以下を保ちつつ、whの最小値を出す

これは以下のようなdpで解ける
dpv[i][bl] = wh → i番目の子まで見て、blの合計がblの時のwhの最小値
O(子の数*Xi)で解けるので、全体ではO(N*max(X))ぐらいで解けるはず
→どうしてもblの合計がXi以下にならない場合、不可能

"""
import sys
from sys import stdin

def dfs(v,p):

    dpB = {}
    dpW = {}
    dpB[0] = 0
    dpW[0] = 0

    for nex in lis[v]:

        if nex != p:
            ndpB = {}
            ndpW = {}
        
            b1,w1,b2,w2 = dfs(nex,v)

            for b in dpB:
                if b+b1 > X[v]:
                    continue
                if b+b1 not in ndpB:
                    ndpB[b+b1] = float("inf")
                ndpB[b+b1] = min(ndpB[b+b1],dpB[b] + w1)
            for b in dpB:
                if b+b2 > X[v]:
                    continue
                if b+b2 not in ndpB:
                    ndpB[b+b2] = float("inf")
                ndpB[b+b2] = min(ndpB[b+b2],dpB[b] + w2)

            for w in dpW:
                if w+w1 > X[v]:
                    continue
                if w+w1 not in ndpW:
                    ndpW[w+w1] = float("inf")
                ndpW[w+w1] = min(ndpW[w+w1] , dpW[w] + b1)
            for w in dpW:
                if w+w2 > X[v]:
                    continue
                if w+w2 not in ndpW:
                    ndpW[w+w2] = float("inf")
                ndpW[w+w2] = min(ndpW[w+w2] , dpW[w] + b2)

            dpB = ndpB
            dpW = ndpW
    
    b1 = X[v]
    w1 = float("inf")
    for i in dpB:
        w1 = min(w1,dpB[i])
    w2 = X[v]
    b2 = float("inf")
    for i in dpW:
        b2 = min(b2,dpW[i])

    if w1 == float("inf") and b2 == float("inf"):
        print ("IMPOSSIBLE")
        sys.exit()

    print (dpB,dpW,file=sys.stderr)
    return b1,w1,b2,w2
                    

N = int(stdin.readline())

P = list(map(int,stdin.readline().split()))
X = list(map(int,stdin.readline().split()))

lis = [ [] for i in range(N) ]
for i in range(1,N):
    lis[i].append(P[i-1]-1)
    lis[P[i-1]-1].append(i)

print(dfs(0,0),file=sys.stderr)
print ("POSSIBLE")
