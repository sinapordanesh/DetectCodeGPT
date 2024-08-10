
"""

https://atcoder.jp/contests/arc097/tasks/arc097_d

始点と終点関係ある？
→逆にしても問題はない

黒い葉は完全に無視できる(落とせる)
よって、葉はすべて白
葉以外は白黒どっちもあり得る

すべての葉をめぐる最短経路？
ある葉からスタートするのは自明っぽい？
ある白からスタートするのはそう

→自分を塗ってからdfsする
→全方位木dp?

行きのみで帰らない場所が1つ存在するはず
→始点と終点のパスとそこから生える木って感じのイメージ

足踏み(停止)の回数を極力少なくしたい
→始点でも終点でもない場合、 e本の辺がつながってたらe回訪問は確定
　e^colorが黒でない場合は+1
→つまり、各頂点で消費する回数は始点・終点でない限り常に一定？

終点はまず葉→始点も葉でおｋ
始点は足踏みなので1秒つかう　終点も1秒使う
パス上の点は、e-1回訪問(ここが根本的に違う！)

つまり、あるパスがあって　その長さがL(両端除く)の時、最大でL減る
ただし、パス上にあっても回数が減らない点もある

B=0 W=1とするか
(color^E) == 1 の点は、E-1回訪問になると足踏みがいらないから2減る
つまり、そのような点が最大数あるパスを求めればいい

"""

import sys
sys.setrecursionlimit(200000)
from collections import deque

MM = 0

def dfs(v,p):
    global MM

    if v != p and linknum[v] == 1:
        return 0

    cl = []
    for nex in lis[v]:
        if nex != p and exist[nex]:
            tmp = dfs(nex,v)
            cl.append(tmp)
    cl.sort()
    cl.reverse()

    if len(cl) == 1:
        MM = max(MM , cl[0])
    else:
        if (linknum[v]+c[v])%2 == 1:
            MM = max(MM , cl[0] + cl[1] + 2)
        else:
            MM = max(MM , cl[0] + cl[1])

    
    if (linknum[v]+c[v]) % 2 == 1:
        return cl[0]+ 2
    else:
        return cl[0]

N = int(input())

lis =  [ [] for i in range(N) ]
linknum = [0] * N
for i in range(N-1):
    u,v = map(int,input().split())
    u -= 1
    v -= 1

    lis[u].append(v)
    lis[v].append(u)
    linknum[u] += 1
    linknum[v] += 1

ctmp = input()
c = []

for i in ctmp:
    if i == "B":
        c.append(0)
    else:
        c.append(1)

exist = [True] * N

q = deque([])
for i in range(N):
    if linknum[i] <= 1 and c[i] == 0:
        q.append(i)

while len(q) > 0:
    now = q.popleft()
    exist[now] = False
    linknum[now] = 0
    
    for nex in lis[now]:
        linknum[nex] -= 1

        if linknum[nex] == 1 and c[nex] == 0:
            q.append(nex)

#print (exist)
start = None
for i in range(N):
    if exist[i]:
        start = i
        break
else:
    print (0)
    sys.exit()

if linknum[start] == 0:
    print (1)
    sys.exit()

ans = 0
#print (linknum)
for i in range(N):
    if exist[i]:

        if (linknum[i] + c[i]) % 2 == 0:
            ans += linknum[i]
        else:
            ans += linknum[i] + 1

MM = 0
pick = dfs(start,start)
print (ans - MM)
