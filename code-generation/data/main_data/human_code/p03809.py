
"""

https://atcoder.jp/contests/agc010/tasks/agc010_c

似たような問題を最近やらなかったっけ…？
→Complete Compressか

部分木に注目してみる

部分木から飛び出すパスの個数をXとしてみよう
余ったパスは上に投げるしかない
→部分木から飛び出すパスの本数の最小をYとすると、Y[根] == 0 が答え
根は葉でない頂点を適当に選ぶ

飛び出すパスの本数の最小はどう計算するか？
最大と最小を受け取る
いい感じにつなげて最小と最大を導出したい

まず、最大・最小間はすべて作れるのか？
2本飛び出している奴を接続すると、飛び出しは2減り、1余るので飛び出しが1ふえる…？
→もしかして飛び出し本数の候補はより少ない？

容量が X で、子が全部葉、 a,bとする
n組繋げたとすると、 a+b-2n 本飛び出す
X = n + (a+b-2n) = a+b-n
なので、nは一定値になる n = a+b-X
nは、最小は0、最大は過半数でなければa+b+…　にでき、そうでなければ最大値以外の和の範囲を取れる
nがその条件を満たしているかを調べればいい

"""

from sys import stdin
import sys
sys.setrecursionlimit(200000)

def dfs(v,p):
    if len(lis[v]) == 1:
        return A[v]

    chlis = []
    for nex in lis[v]:
        if nex != p:
            chlis.append(dfs(nex,v))
    chlis.sort()
    chsum = sum(chlis)

    n = chsum - A[v]
    if chlis[-1] * 2 <= chsum:
        if 0 <= n <= chsum//2:
            pass
        else:
            print ("NO")
            sys.exit()
    else:
        if 0 <= n <= chsum-chlis[-1]:
            pass
        else:
            print ("NO")
            sys.exit()
    return chsum - 2 * n

N = int(stdin.readline())

A = list(map(int,stdin.readline().split()))
if N == 2:
    if A[0] == A[1]:
        print ("YES")
    else:
        print ("NO")
    sys.exit()

lis = [ [] for i in range(N)]

for loop in range(N-1):
    u,v = map(int,stdin.readline().split())
    u -= 1
    v -= 1
    lis[u].append(v)
    lis[v].append(u)

root = None
for i in range(N):
    if len(lis[i]) > 1:
        root = i
        break

ret = dfs(root,root)
if ret == 0:
    print ("YES")
else:
    print ("NO")

