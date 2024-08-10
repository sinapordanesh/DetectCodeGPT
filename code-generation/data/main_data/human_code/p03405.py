
"""

https://atcoder.jp/contests/arc093/tasks/arc093_c

各辺を含む最小全域木を考える
→重みがX未満なら、その全域木に含まれる辺は全て同一色で塗る必要がある

全ての辺に対してやれば十分？
→ではない

むしろ、X未満の全域木となった辺すべて同一色で塗る必要がある？
辺A,Bを含む全域偽は重みがX未満だが、同一色で塗る必要がないとする
→AとBの最小全域木は共有辺を一切持たない
A,Bを二つの頂点集合に分ける。頂点集合間は、別の辺l,Lで結ばれている
元の辺を除いた重みの輪を a,bとすると、 a+l < X  b+L < X である
よって、辺を交換するとどちらかは必ずX未満となる
→よって、その辺を含む最小全域木

AとBの辺を少なくとも1つづつ含む最小全域木が存在することを示せばいい
最小の重みの辺LがAにあるとする
Lに接続されている頂点Xには、Bの辺が1本ささっている
この辺を含む最小全域木をクラスカル法で構築していくと、Aの最小の辺を絶対含む
→よって、ただしい

まず、各辺を含む最小全域木を考え、重みがX未満なら白で塗る
重みがXを超える場合、重みXの全域木に含まれることはないため好きな色で塗る
→不要なため以後グラフに無いものとして扱う

今グラフには白い辺(X未満)と、未定(X)の辺がある
塗分け方は 2^X である。ここから補集合(Xの全域木を構成できない場合)を引く
全部白の場合は自明に無理

白で塗られた辺が1つ以上存在する場合を考える
黒が1つでも入っていれば構成可能？
→最小全域木に必ず白を含むことを証明できれば良い
未定の辺の最小 >= 白い辺の最小 が示せれば、白い辺の片方の頂点に来た時に絶対選ばれるのでおｋ
未定の辺が最小だった場合、片方に来た時に選ばれてしまうので示された

入っていない場合、すべて同一色でなければ構成可能？
→これも同様に証明可能なはず

"""

from sys import stdin
import sys

def uf_find(n,p):

    ufl = []

    while p[n] != n:
        ufl.append(n)
        n = p[n]

    for i in ufl:
        p[i] = n

    return n


def uf_union(a,b,p,rank):

    ap = uf_find(a,p)
    bp = uf_find(b,p)

    if ap == bp:
        return False
    else:

        if rank[ap] > rank[bp]:
            p[bp] = ap
        elif rank[ap] < rank[bp]:
            p[ap] = bp
        else:
            p[bp] = ap
            rank[ap] += 1

        return True

N,M = map(int,stdin.readline().split())

X = int(stdin.readline())

wvu = []

for i in range(M):

    u,v,w = map(int,stdin.readline().split())
    wvu.append((w,v-1,u-1))

overX = 0
justX = 0
underX = 0
wvu.sort()

for i in range(M):

    p = [i for i in range(N)]
    rank = [0] * N
    h = 0

    h += wvu[i][0]
    uf_union(wvu[i][1],wvu[i][2],p,rank)

    for j in range(M):

        if uf_union(wvu[j][1],wvu[j][2],p,rank):
            h += wvu[j][0]

    if h > X:
        overX += 1
    elif h == X:
        justX += 1
    else:
        underX += 1

print (overX,justX,underX,file=sys.stderr)
ans = 0
mod = 10**9+7

if justX == 0:
    ans = 0
elif underX > 0:
    ans = 2 * pow(2,overX,mod) * (pow(2,justX,mod)-1)
else:
    ans = pow(2,overX,mod) * (pow(2,justX,mod)-2)

print (ans % mod)
