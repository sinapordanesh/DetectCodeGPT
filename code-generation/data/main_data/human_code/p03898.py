import sys
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

"""
・次数3以上の点は使わないとしてよい
・次数1の点は全て回収できる。次数2の点を、パスとなる形で回収する。
"""

N = int(readline())
PQ = [tuple(int(x)-1 for x in line.split()) for line in readlines()]

graph = [[] for _ in range(N)]
for p,q in PQ:
    graph[p].append(q)
    graph[q].append(p)    

deg = [len(x) for x in graph]

cnt_deg1 = sum(x==1 for x in deg)

deg2_path = 0

def dfs(x,parent):
    global deg2_path
    # 部分木で完結する場合、しない場合
    arr = [dfs(y,x) for y in graph[x] if y != parent]
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0] + (deg[x] == 2)
    arr.sort()
    deg2_path = max(deg2_path, arr[-1] + arr[-2] + (deg[x]==2))
    return arr[-1] + (deg[x] == 2)

dfs(0,-1)
answer = cnt_deg1 + deg2_path
print(answer)