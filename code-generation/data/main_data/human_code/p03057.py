
"""

https://atcoder.jp/contests/agc033/tasks/agc033_e

Sの1文字目をRとしてよい

RB  から始まる場合　→ 全部交互以外無理(Nが奇数なら0)
RRB から始まる場合　→ Rは3連で置けば可能…

R*X + B*Y + R*Z …
とつながっていく

どこからスタートしても、RだけをX回移動したときにBの隣に来なくてはいけない
Rの長さが1なら可能

R*?,B,R*?,…
でつながっていく

最初のRがX個連続の時
片方の端との距離がX-2tでなくてはならない
Xが偶数の時、Rの連続長さはX+1以下の奇数
Xが奇数の時、端からスタートした奴は反対側に抜けなくてはいけないので
Rの連続長さはX以下の奇数？
結局は奇数個連続でしか置けない


●整理(Rから始まり、Bがある場合)：
Rは奇数個連続でしか置けない
Bは1個連続でしか置けない
→つまり、Nが奇数だとアウト


Bが来た以降を考えてみる
奇数だと、各点Rの左右のどちらかにしか抜けられない→対称的な移動になるはず
→つまり、最初のRを消化した後、全てのBの両端にいる場合が存在する

Bは奇数個の時のみ意味がある
→結局、Bの両端にいた場合が交換されるだけ
→よって、BはRの区切り以上の意味はない

Rが偶数個来るた場合、交互に移動すればおk
Rが奇数個来た場合、反対側に抜ける必要がある

結論：
RBがどちらも存在する場合、Nが偶数なら0、奇数の場合は
BでsplitしたRの個数の集合を考え,
r1,r2…,r? とする
Rは奇数個連続で置けて、その個数の最大は M = min( r1+1 , r? ) #r?が奇数の物
後は、M+1個以下の偶数個単位で区切る場合の数を調べればいい
dp→あらかじめ1番目の区間の位置に、ずれた分も考慮して値を入れておけばBITでもらうdpできる

RB片方の場合、Bが連続しないような置き方をすればいい
1番目がRの場合をdp → N番目までやる
1番目がBの場合をdp → N-1番目までやる(N番目は赤なので)

最後のRは意味がないので消しておく


REの原因究明したい
K < NNの場合？


"""

from sys import stdin
import sys
#0-indexed , 半開区間[a,b)
#calc変更で演算変更
class SegTree:

    def __init__(self,N,first):
        self.NO = 2**(N-1).bit_length()
        self.First = first
        self.data = [first] * (2*self.NO)

    def calc(self,l,r):
        return (l+r) % mod

    def update(self,ind,x):
        ind += self.NO - 1
        self.data[ind] = x
        while ind >= 0:
            ind = (ind - 1)//2
            self.data[ind] = self.calc(self.data[2*ind+1],self.data[2*ind+2])

    def query(self,l,r):
        L = l + self.NO
        R = r + self.NO
        s = self.First
        while L < R:
            if R & 1:
                R -= 1
                s = self.calc(s , self.data[R-1])
            if L & 1:
                s = self.calc(s , self.data[L-1])
                L += 1
            L >>= 1
            R >>= 1
        return s

    def get(self , ind):
        ind += self.NO - 1
        return self.data[ind]

N,M = map(int,stdin.readline().split())
S = list(stdin.readline()[:-1])
mod = 10**9+7

if "R" in S and "B" in S:

    if N % 2 == 1:
        print (0)
        sys.exit()

    lis = []
    now = 0
    while S[-1] == S[0]: #最後のRを消す
        del S[-1]
    for i in S:
        if i == S[0]:
            now += 1
        elif now > 0:
            lis.append(now)
            now = 0
    #print (lis)

    nmax = 0
    for i in range(len(lis)):
        if i == 0:
            if lis[i] % 2 == 0:
                nmax = lis[i] + 1
            else:
                nmax = lis[i]
        elif lis[i] % 2 == 1:
            nmax = min(nmax , lis[i])

    NN   = N//2
    K    = (nmax+1)//2
    print (NN,K,file=sys.stderr)

    if NN <= K:
        print ((pow(2,NN,mod)-1) * 2 % mod)
        sys.exit()

    ST = SegTree(NN,0)
    for i in range(K):
        ST.update(i,i+1)

    for i in range(1,NN):
        now = ST.get(i)
        plus = ST.query( max(0,i-K),i )
        ST.update( i , (now+plus) % mod )

    print (ST.get(NN-1) * 2 % mod)
        
else:

    ans = 0
    #1番目がRの場合
    dp = [1,0]
    for i in range(N-1):
        ndp = [0,0]
        ndp[0] = (dp[0] + dp[1]) % mod
        ndp[1] = dp[0]
        dp = ndp

    ans += sum(dp)

    #1番目がBの場合
    dp = [0,1]
    for i in range(N-2):
        ndp = [0,0]
        ndp[0] = (dp[0] + dp[1]) % mod
        ndp[1] = dp[0]
        dp = ndp
    ans += sum(dp)

    print (ans % mod)