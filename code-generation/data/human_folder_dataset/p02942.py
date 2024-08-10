
"""

https://atcoder.jp/contests/agc037/tasks/agc037_d

まず分かりやすさのため全部-1してMで割る
2番目の操作後に上から0行目には全部0 , 1行目には全部1…となればおk

すなわち、1番目の操作では各列に1個づつ数字が入るようにする必要がある
→これは貪欲にやればok・・・じゃない

ある列をうまくはめれば必ず次も可能？
→最後の列を考えると、足りない要素と残りの要素のsetは等しいのでokそう
→2部マッチング！

=====解説=====

そもそも何をマッチングさせてた？
→各行の置けるaとa
→   次数は不定 & 不定
→　Hallが成り立つと証明できない…
→　あれ???????正解解法もおかしくないか

"""

from collections import defaultdict
from collections import deque

route = []

def Ford_Fulkerson_Func(s,g,lines,cost):

    global route
    N = len(cost)
    ans = 0
    queue = deque([ [s,float("inf")] ])

    ed = [True] * N
    ed[s] = False

    route = [0] * N
    route[s] = -1

    while queue:

        now,flow = queue.pop()
        for nex in lines[now]:

            if ed[nex]: 
                flow = min(cost[now][nex],flow)
                route[nex] = now
                queue.append([nex,flow])
                ed[nex] = False

                if nex == g:
                    ans += flow
                    break
            
        else:
            continue
        break

    else:
        return False,ans


    t = g
    s = route[t]

    while s != -1:
        cost[s][t] -= flow
        if cost[s][t] == 0:
            lines[s].remove(t)

        if cost[t][s] == 0:
            lines[t].add(s)
        cost[t][s] += flow
        t = s
        s = route[t]

    return True,ans

def Ford_Fulkerson(s,g,lines,cost):

    ans = 0

    while True:
        fl,nans = Ford_Fulkerson_Func(s,g,lines,cost)

        if fl:
            ans += nans
            continue
        else:
            break
    
    return ans


from sys import stdin
import sys
sys.setrecursionlimit(10000)

N,M = map(int,stdin.readline().split())
B = [[None] * M for i in range(N)]

Bs = [[True] * M for i in range(N)]

A = []
for loop in range(N):

    a = list(map(int,stdin.readline().split()))
    A.append(a)

for loop in range(M):

    lines = defaultdict(set)
    cost = [ [0] * (2*N+2) for i in range(2*N+2) ]

    for i in range(N):
        lines[2*N].add(i)
        cost[2*N][i] = 1
    for i in range(N,2*N):
        lines[i].add(2*N+1)
        cost[i][2*N+1] = 1
    for i in range(N):
        for j in range(len(A[i])):
            lines[i].add((A[i][j]-1)//M + N)
            cost[i][(A[i][j]-1)//M + N] = 1

    Ford_Fulkerson(2*N,2*N+1,lines,cost)
    ans = []

    for i in range(N):
        for j in range(len(A[i])):
            if cost[i][(A[i][j]-1)//M + N] == 0:
                ans.append(A[i][j])
                del A[i][j]
                break
    #print (ans)
    for i in range(N):
        B[i][loop] = ans[i]
                

for i in B:
    print (*i)

C = [[None] * M for i in range(N)]
for j in range(M):
    tmp = []
    for i in range(N):
        tmp.append(B[i][j])
    tmp.sort()
    for i in range(N):
        C[i][j] = tmp[i]

for i in C:
    print (*i)
